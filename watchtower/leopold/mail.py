import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from watchtower.leopold import html, settings
from watchtower.leopold.client import get_url

NAVER_MAIL_SMTP_URL = "smtp.naver.com"
NAVER_MAIL_SMTP_SECURE_PORT = 587


def build_html_content(tid: str) -> str:
    url = get_url(tid)
    path = settings.DATA_DIR / "email_template.html"
    with open(path) as html_file:
        html_ = html.to_html(html_file.read())
        a = html_.css_first("a#destination")
        a.attrs["href"] = url
        return html_.html


def build_message(tid: str) -> MIMEMultipart:
    message = MIMEMultipart()
    message["From"] = settings.NAVER_MAIL_USER
    message["To"] = settings.GMAIL_USER
    message["Subject"] = "FC660M BT 영문 판매 시작"
    content = build_html_content(tid)
    message.attach(MIMEText(content, "html"))
    return message


def send_email(tid: str) -> None:
    with smtplib.SMTP(NAVER_MAIL_SMTP_URL, port=NAVER_MAIL_SMTP_SECURE_PORT) as server:
        server.starttls()
        server.login(settings.NAVER_MAIL_USER, settings.NAVER_MAIL_PASSWORD)
        message = build_message(tid)
        for address in settings.RECIPIENTS:
            server.sendmail(settings.NAVER_MAIL_USER, address, message.as_string())
