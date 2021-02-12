from io import TextIOWrapper

import pytest
from selectolax.parser import HTMLParser

from watchtower.leopold import settings


@pytest.fixture
def tid() -> str:
    yield "1550022131"


@pytest.fixture
def leopold_sold_out() -> TextIOWrapper:
    with open(settings.DATA_DIR / "leopold_sold_out.html") as html_file:
        yield html_file


@pytest.fixture
def leopold_sold_out_html(leopold_sold_out) -> HTMLParser:
    yield HTMLParser(leopold_sold_out.read())


@pytest.fixture
def leopold_in_stock() -> TextIOWrapper:
    with open(settings.DATA_DIR / "leopold_in_stock.html") as html_file:
        yield html_file


@pytest.fixture
def leopold_in_stock_html(leopold_in_stock) -> HTMLParser:
    yield HTMLParser(leopold_in_stock.read())


@pytest.fixture
def email_content() -> TextIOWrapper:
    with open(settings.DATA_DIR / "email_template.html") as html_file:
        yield html_file
