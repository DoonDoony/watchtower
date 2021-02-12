from unittest import mock

from pytest_httpx import HTTPXMock

from watchtower.leopold.main import is_available, main


def test_is_not_available(tid, httpx_mock: HTTPXMock, leopold_sold_out):
    httpx_mock.add_response(data=leopold_sold_out.read())
    assert is_available(tid) is False


def test_is_available(tid, httpx_mock: HTTPXMock, leopold_in_stock):
    httpx_mock.add_response(data=leopold_in_stock.read())
    assert is_available(tid) is True


@mock.patch("watchtower.leopold.main.is_available")
def test_send_email_if_available(mock_available, tid):
    mock_available.return_value = True
    with mock.patch("watchtower.leopold.main.send_email") as mock_send_email:
        main()
        mock_send_email.assert_called_with(tid)


@mock.patch("watchtower.leopold.main.is_available")
def test_should_not_send_email_if_is_not_available(mock_available, tid):
    mock_available.return_value = False
    with mock.patch("watchtower.leopold.main.send_email") as mock_send_email:  # type: mock.MagicMock
        main()
        mock_send_email.assert_not_called()
