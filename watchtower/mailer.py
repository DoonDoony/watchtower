import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

from watchtower import settings
from watchtower.leopold import html

NAVER_MAIL_SMTP_URL = "smtp.naver.com"
NAVER_MAIL_SMTP_SECURE_PORT = 587


class Mailer:
    template = settings.TEMPLATE_DIR / "email_template.html"

    def __init__(self) -> None:
        self._content = ""
        self._message = MIMEMultipart()

    def build_html_content(self, destination: str) -> "Mailer":
        with open(self.template) as html_file:
            html_ = html.to_html(html_file.read())
            a = html_.css_first("a#destination")
            a.attrs["href"] = destination
            self._content = html_.html
            return self

    def build_message(self, subject: str) -> "Mailer":
        self._message["From"] = settings.NAVER_MAIL_USER
        self._message["To"] = settings.GMAIL_USER
        self._message["Subject"] = subject
        self._message.attach(MIMEText(self.content, "html"))
        return self

    def send_email(self, url: str, subject: str, recipients: List[str]) -> None:
        with smtplib.SMTP(NAVER_MAIL_SMTP_URL, port=NAVER_MAIL_SMTP_SECURE_PORT) as server:
            server.starttls()
            server.login(settings.NAVER_MAIL_USER, settings.NAVER_MAIL_PASSWORD)
            self.build_html_content(url).build_message(subject)
            for address in recipients:
                server.sendmail(settings.NAVER_MAIL_USER, address, self.message.as_string())

    @property
    def content(self) -> str:
        return self._content

    @property
    def message(self) -> MIMEMultipart:
        return self._message


mailer = Mailer()
