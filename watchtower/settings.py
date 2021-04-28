import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent  # watchtower
TEMPLATE_DIR = BASE_DIR / "templates"
ENV_FILE = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_FILE)

NAVER_MAIL_USER = os.getenv("NAVER_MAIL_USER", "")
NAVER_MAIL_PASSWORD = os.getenv("NAVER_MAIL_PASSWORD", "")
GMAIL_USER = os.getenv("GMAIL_USER", "")

RECIPIENTS = os.getenv("LEOPOLD_RECIPIENTS", "").split(",")
