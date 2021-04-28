import os
from unittest import mock

import pytest


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    with mock.patch.dict(os.environ, {"SMOKETIGERS_RECIPIENTS": "godori@godori.dev"}):
        yield
