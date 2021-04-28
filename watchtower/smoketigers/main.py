import os

import httpx

from watchtower.mailer import mailer


def main() -> None:
    url = "https://smokingtigers.co.kr/product/gt-ss-tee-khaki/295/category/63/display/1/"
    response = httpx.get(url)
    if "품절" not in response.text:
        subject = "티셔츠 판매가 시작되었습니다."
        recipients = os.getenv("SMOKETIGERS_RECIPIENTS", "").split(",")
        mailer.send_email(url, subject, recipients)
