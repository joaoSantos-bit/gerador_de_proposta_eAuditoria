from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from typing import Optional
from .utils.pptx_generator import PPTXGenerator
from app.utils.cloud_convert_service import convert_to_pdf
import json
import os
import csv
import httpx
from io import StringIO

# Load environment variables
load_dotenv()

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates configuration
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/form/{form_id}", response_class=HTMLResponse)
async def form(request: Request, form_id: int):
    if form_id not in [1, 2, 3, 4]:
        return templates.TemplateResponse("error.html", {
            "request": request,
            "message": "Formulário inválido"
        })

    SHEET_ID = os.getenv("SHEET_ID")  # exemplo: '1AbCDeFGhIjKLmnopQrStUVwxyz1234567890'
    GID = "655425745"  # ajuste conforme necessário
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={GID}"
    vendedores = []
    async with httpx.AsyncClient() as client:
        response = await client.get(url, follow_redirects=True)

        if response.status_code == 200:
            csv_content = response.text
            csv_reader = csv.reader(StringIO(csv_content))
            next(csv_reader)  # pular cabeçalho
            for row in csv_reader:
                if row:
                    vendedores.append(row[0])
    return templates.TemplateResponse(
        f"form/{form_id}.html",
        {
            "request": request,
            "form_id": form_id,
            "show_files": form_id in [1, 3],  # Forms 1 e 3 permitem arquivos
            "vendedores": vendedores
        }
    )

@app.post("/generate")
async def generate_proposal(
    request: Request,
    form_id: int = Form(...),
    variables: str = Form(...),
    down1: Optional[UploadFile] = File(None),
    down2: Optional[UploadFile] = File(None),
    down3: Optional[UploadFile] = File(None),
    down4: Optional[UploadFile] = File(None),
    down5: Optional[UploadFile] = File(None),
):

    variables_dict = json.loads(variables)
    files = {
        "down1": down1,
        "down2": down2,
        "down3": down3,
        "down4": down4,
        "down5": down5,
    }

    # Generate PPTX
    pptx_generator = PPTXGenerator(variables_dict, form_id, files)
    pptx_path = await pptx_generator.generate()
    
    # Convert to PDF
    pdf_path = await convert_to_pdf(pptx_path, pptx_path.with_suffix(".pdf"))
    
    # Generate email template
    email_path = pptx_generator.generate_email_template()
    
    # Create ZIP with all files
    zip_path = pptx_generator.create_zip(pptx_path, pdf_path, email_path)
    
    return FileResponse(
        zip_path,
        media_type="application/zip",
        filename="proposta e-Auditoria.zip"
    )