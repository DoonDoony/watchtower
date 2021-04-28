from textwrap import dedent
from unittest import mock

import pytest

from watchtower.mailer import Mailer


@pytest.fixture
def mailer() -> Mailer:
    yield Mailer()


@pytest.fixture
def url() -> str:
    yield "http://localhost:65535"


def test_mailer_build_html_content(mailer: Mailer, url: str):
    expected_html = dedent(
        f"""\
        <html lang="ko"><head>
            <meta charset="UTF-8">
        </head>
        <body>
            <p>아래 홈페이지에서 빨리 확인하고 구매하세요 🏃‍♂️</p>
            <a id="destination" href="{url}">제품 페이지로 이동</a>


        </body></html>
        """
    )

    mailer.build_html_content(url)
    assert url in mailer.content
    assert mailer.content == expected_html.strip()


def test_mailer_build_message(mailer: Mailer, url: str):
    subject = "Title"
    mailer.build_html_content(url).build_message(subject)
    assert subject == mailer.message.get("Subject")


@mock.patch("watchtower.mailer.smtplib.SMTP")
def test_send_email(mock_smtp: mock.MagicMock, mailer: Mailer, url: str):
    recipients = ["dooon@dev.null", "doon@dev.null"]
    with mock_smtp("smtp.naver.com", port=587) as server:
        mailer.send_email(url, "Title", recipients)
        assert server.sendmail.call_count == len(recipients)
        for call in server.sendmail.mock_calls:
            from_, to, content = call.args
            assert to in recipients
