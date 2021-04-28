import os

from watchtower.leopold import html
from watchtower.leopold.client import get_page, get_url
from watchtower.mailer import mailer


def is_available(tid: str) -> bool:
    page = get_page(tid)
    html_ = html.to_html(page)
    return not bool(html.get_sold_out(html_))


def main() -> None:
    fc_660m_bt = "1550022131"
    if is_available(fc_660m_bt):
        url = get_url(fc_660m_bt)
        recipients = os.getenv("LEOPOLD_RECIPIENTS", "").split(",")
        return mailer.send_email(url, "FC660M BT 영문 판매 시작", recipients)


if __name__ == "__main__":
    main()
