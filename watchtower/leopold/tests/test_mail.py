from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from textwrap import dedent
from unittest import mock

from watchtower.leopold import settings
from watchtower.leopold.mail import build_html_content, build_message, send_email


def test_build_html_content(tid):
    html = build_html_content(tid)
    expected_html = dedent(
        """\
        <html lang="ko"><head>
            <meta charset="UTF-8">
        </head>
        <body>
            <p>아래 홈페이지에서 빨리 확인하고 구매하세요 🏃‍♂️</p>
            <a id="destination" href="https://www.leopold.co.kr/Shop/Item.php?ItId=1550022131">제품 페이지로 이동</a>


        </body></html>
        """
    )
    assert html.strip() == expected_html.strip()


def test_build_message(tid):
    actual_message = build_message(tid)
    message = MIMEMultipart()
    message["From"] = settings.NAVER_MAIL_USER
    message["To"] = settings.GMAIL_USER
    message["Subject"] = "FC660M BT 영문 판매 시작"
    content = build_html_content(tid)
    message.attach(MIMEText(content, "html"))

    assert actual_message["From"] == message["From"]
    assert actual_message["To"] == message["To"]
    assert actual_message["Subject"] == message["Subject"]


@mock.patch("watchtower.leopold.settings.RECIPIENTS")
@mock.patch("watchtower.leopold.mail.smtplib.SMTP")
def test_send_email(mock_smtp: mock.MagicMock, mock_recipients, tid):
    mock_recipients.return_value = ["doon@dev.null", "dooon@dev.null"]
    message = build_message(tid)
    with mock_smtp("smtp.naver.com", port=587) as server:
        send_email(tid)
        assert server.sendmail.call_count == len(mock_recipients)
        for call in server.sendmail.mock_calls:
            from_, to, content = call.args
            server.sendmail.assert_called_with(from_, to, message)
