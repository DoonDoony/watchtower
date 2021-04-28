import os
from io import TextIOWrapper
from unittest import mock

import pytest
from selectolax.parser import HTMLParser

from watchtower import settings


@pytest.fixture
def tid() -> str:
    yield "1550022131"


@pytest.fixture
def leopold_sold_out() -> TextIOWrapper:
    with open(settings.TEMPLATE_DIR / "leopold" / "leopold_sold_out.html") as html_file:
        yield html_file


@pytest.fixture
def leopold_sold_out_html(leopold_sold_out) -> HTMLParser:
    yield HTMLParser(leopold_sold_out.read())


@pytest.fixture
def leopold_in_stock() -> TextIOWrapper:
    with open(settings.TEMPLATE_DIR / "leopold" / "leopold_in_stock.html") as html_file:
        yield html_file


@pytest.fixture
def leopold_in_stock_html(leopold_in_stock) -> HTMLParser:
    yield HTMLParser(leopold_in_stock.read())


@pytest.fixture
def email_content() -> TextIOWrapper:
    with open(settings.TEMPLATE_DIR / "email_template.html") as html_file:
        yield html_file


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    with mock.patch.dict(os.environ, {"LEOPOLD_RECIPIENTS": "doon@dev.null,doondoony@dev.null"}):
        yield
