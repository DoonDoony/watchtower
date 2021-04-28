from unittest import mock

from pytest_httpx import HTTPXMock

from watchtower.smoketigers.main import main


def test_send_email_if_available(httpx_mock: HTTPXMock):
    httpx_mock.add_response(data="재고 있음".encode())
    with mock.patch("watchtower.smoketigers.main.mailer") as mock_mailer:
        url = "https://smokingtigers.co.kr/product/gt-ss-tee-khaki/295/category/63/display/1/"
        subject = "티셔츠 판매가 시작되었습니다."
        recipients = ["godori@godori.dev"]
        main()
        mock_mailer.send_email.assert_called_with(url, subject, recipients)


def test_send_email_if_unavailable(httpx_mock: HTTPXMock):
    httpx_mock.add_response(data="품절".encode())
    with mock.patch("watchtower.smoketigers.main.mailer") as mock_mailer:
        main()
        mock_mailer.send_email.assert_not_called()
