import supabase
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def upload_resume(file: str):
    client = supabase.create_client(
        SUPABASE_URL,
        SUPABASE_KEY,
    )
    with open(file, 'rb') as file_to_upload:
        response = client.storage.from_("application_resumes").upload(
            "resume.pdf", file_to_upload
        )
        print(response)
