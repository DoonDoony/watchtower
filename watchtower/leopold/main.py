from watchtower.leopold import html
from watchtower.leopold.client import get_page
from watchtower.leopold.mail import send_email


def is_available(tid: str) -> bool:
    page = get_page(tid)
    html_ = html.to_html(page)
    return not bool(html.get_sold_out(html_))


def main() -> None:
    fc_660m_bt = "1550022131"
    if is_available(fc_660m_bt):
        return send_email(fc_660m_bt)


if __name__ == "__main__":
    main()
