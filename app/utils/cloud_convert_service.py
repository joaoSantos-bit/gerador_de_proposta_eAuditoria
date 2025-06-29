import httpx
import asyncio
import os
from typing import Dict, Any
from pathlib import Path

API_KEY = os.getenv("PDF_CONVERT_API_KEY")

BASE_HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

async def create_job() -> Dict[str, Any]:
    url = "https://api.cloudconvert.com/v2/jobs"
    data = {
        "tasks": {
            "upload-my-file": {
                "operation": "import/upload"
            },
            "convert-my-file": {
                "operation": "convert",
                "input": "upload-my-file",
                "input_format": "pptx",
                "output_format": "pdf"
            },
            "export-my-file": {
                "operation": "export/url",
                "input": "convert-my-file"
            }
        }
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=BASE_HEADERS)
        response.raise_for_status()
        return response.json()["data"]

async def upload_file(upload_task: dict, filename: str):
    upload_url = upload_task["result"]["form"]["url"]
    upload_params = upload_task["result"]["form"]["parameters"]

    path = Path(filename)
    with open(path, "rb") as f:
        files = {
            'file': (str(path.name), f, 'application/vnd.openxmlformats-officedocument.presentationml.presentation')
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(upload_url, data=upload_params, files=files)
            response.raise_for_status()

async def wait_for_job(job_id: str) -> Dict[str, Any]:
    url = f"https://api.cloudconvert.com/v2/jobs/{job_id}"
    async with httpx.AsyncClient() as client:
        while True:
            response = await client.get(url, headers=BASE_HEADERS)
            response.raise_for_status()
            job = response.json()["data"]
            status = job["status"]
            if status == "finished":
                return job
            elif status == "error":
                raise Exception("Conversão falhou")
            await asyncio.sleep(3)

async def download_file(export_task: Dict[str, Any], output_filename: str):
    file_url = export_task["result"]["files"][0]["url"]
    async with httpx.AsyncClient() as client:
        response = await client.get(file_url)
        response.raise_for_status()
        with open(output_filename, "wb") as f:
            f.write(response.content)

async def convert_to_pdf(input_file: str, output_file: str) -> str:
    job = await create_job()

    upload_task = next(task for task in job["tasks"] if task["name"] == "upload-my-file")
    await upload_file(upload_task, input_file)

    job = await wait_for_job(job["id"])
    export_task = next(task for task in job["tasks"] if task["name"] == "export-my-file")
    await download_file(export_task, output_file)

    return output_file
