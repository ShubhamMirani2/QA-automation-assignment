from dotenv import load_dotenv
import os
from pathlib import Path

# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file
load_dotenv(BASE_DIR / ".env")

BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("USER_CRED")
PASSWORD = os.getenv("PASS_CRED")

print("BASE_URL:", BASE_URL)
print("USERNAME:", USERNAME)
print("PASSWORD:", PASSWORD)