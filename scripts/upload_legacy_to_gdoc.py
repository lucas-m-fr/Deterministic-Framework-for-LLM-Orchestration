import os
import json
import base64
from pathlib import Path
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# --- CONFIGURATION ---
SERVICE_ACCOUNT_FILE = r"D:\OneDrive\Brains\APIs & MCPs\Google Services\gmail-498408-9bef9ce1802c.json"
DOCUMENT_ID = "1B-fb7f1cFdqiO24FH9vD3hM3d_QN1BdEh05iI2uAQmI"
SOURCE_FILE = r"C:\Users\Pramish\AppData\Local\Temp\claude\brainos-repo\BRAINOS_LEGACY_DOCUMENTATION.md"
# ----------------------

def upload_to_gdoc():
    print("[Upload] Initializing Google Docs API connection...")
    try:
        # Authenticate using the Service Account key
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, 
            scopes=["https://www.googleapis.com/auth/documents"]
        )
        service = build('docs', 'v1', credentials=creds)

        # Read the legacy documentation
        with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

        print(f"[Upload] Reading {SOURCE_FILE}...")
        
        # To write to a Google Doc, we must send a batch of 'requests'
        # This script appends the content to the end of the document
        requests = [
            {
                'insertText': {
                    'location': {'index': 1},
                    'text': content
                }
            }
        ]

        print(f"[Upload] Writing to Google Doc {DOCUMENT_ID}...")
        service.execute(batchUpdate(
            documentId=DOCUMENT_ID,
            body={'requests': requests}
        ))
        
        print("[Success] The BrainOS Legacy Archive has been successfully uploaded to your Google Doc.")

    except Exception as e:
        print(f"[Error] Failed to upload to Google Docs: {e}")

if __name__ == "__main__":
    upload_to_gdoc()
