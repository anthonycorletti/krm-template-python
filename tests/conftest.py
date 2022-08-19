from typing import Generator

import pytest
from fastapi.testclient import TestClient

from krm_template_python.main import api


@pytest.fixture()
def client() -> Generator:
    with TestClient(api) as client:
        yield client
