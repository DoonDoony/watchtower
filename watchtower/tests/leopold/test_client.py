from http.client import BAD_REQUEST

import pytest
from httpx import HTTPStatusError
from pytest_httpx import HTTPXMock

from watchtower.leopold.client import get_page, get_param_with_tid, get_url


def test_get_param_with_tid(tid):
    assert get_param_with_tid(tid) == {"ItId": tid}


def test_get_url(tid):
    url = f"https://www.leopold.co.kr/Shop/Item.php?ItId={tid}"
    assert get_url(tid) == url


def test_get_page_with_ok(tid, httpx_mock: HTTPXMock, leopold_in_stock):
    mock_page = leopold_in_stock.read()
    httpx_mock.add_response(data=mock_page)
    page = get_page(tid)
    assert page == mock_page


def test_get_page_with_bad_request(tid, httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=BAD_REQUEST)
    with pytest.raises(HTTPStatusError):
        get_page(tid)
