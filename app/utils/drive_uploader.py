from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import os
from pathlib import Path
import io

SCOPES = ["https://www.googleapis.com/auth/drive"]
FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CREDENTIALS_PATH = BASE_DIR / "credentials.json"

creds = service_account.Credentials.from_service_account_file(
    str(CREDENTIALS_PATH), scopes=SCOPES
)
drive_service = build("drive", "v3", credentials=creds)

async def upload_file_to_drive(file_path: str, file_name: str) -> str:
    file_metadata = {
        "name": file_name,
        "parents": [FOLDER_ID],
    }
    media = MediaFileUpload(file_path, resumable=True)
    uploaded_file = (
        drive_service.files()
        .create(body=file_metadata, media_body=media, fields="id")
        .execute()
    )

    # Tornar público
    drive_service.permissions().create(
        fileId=uploaded_file["id"], body={"role": "reader", "type": "anyone"}
    ).execute()

    return f"https://drive.google.com/file/d/{uploaded_file['id']}/view?usp=sharing"


async def download_file_from_drive(file_name: str) -> str:
    # Busca o arquivo pelo nome dentro da pasta
    query = f"'{FOLDER_ID}' in parents and name = '{file_name}' and trashed = false"
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    items = results.get("files", [])

    if not items:
        raise FileNotFoundError(f"Arquivo '{file_name}' não encontrado na pasta do Drive.")

    file_id = items[0]["id"]

    # Caminho local para salvar o arquivo
    output_path = BASE_DIR / "downloads" / file_name
    os.makedirs(output_path.parent, exist_ok=True)

    request = drive_service.files().get_media(fileId=file_id)
    fh = io.FileIO(output_path, "wb")
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()

    return str(output_path)