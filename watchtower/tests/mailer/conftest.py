from io import TextIOWrapper

import pytest

from watchtower import settings


@pytest.fixture
def email_content() -> TextIOWrapper:
    with open(settings.TEMPLATE_DIR / "email_template.html") as html_file:
        yield html_file
