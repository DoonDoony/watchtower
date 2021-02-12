from typing import Dict

import furl
import httpx
from httpx import Response

BASE_URL = "https://www.leopold.co.kr/Shop/Item.php"


def get_param_with_tid(tid: str) -> Dict[str, str]:
    return {"ItId": tid}


def get_url(tid: str) -> str:
    params = get_param_with_tid(tid)
    url = furl.furl(BASE_URL)
    return url.add(params).url


def _get(url: str) -> Response:
    with httpx.Client() as client:
        return client.get(url)


def get_page(tid: str) -> str:
    url = get_url(tid)
    response = _get(url)
    response.raise_for_status()

    return response.text
