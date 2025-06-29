from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
from pathlib import Path

SCOPES = ["https://www.googleapis.com/auth/drive"]
FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")  # Defina no seu .env

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
