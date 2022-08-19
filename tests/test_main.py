from datetime import datetime
from typing import Any

from fastapi.testclient import TestClient

import krm_template_python.gunicorn_config as gunicorn_config
from krm_template_python import __version__
from krm_template_python.logger import logger


def test_healthz(client: TestClient) -> None:
    response = client.get("/healthz")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json.get("message") == "We're on the air."


def test_gunicorn_config() -> None:
    assert gunicorn_config.worker_class == "uvicorn.workers.UvicornWorker"


def test_logger(capsys: Any) -> None:
    logger.exception("this is an exception")

    logger.info(
        "testing types",
        extra={
            "string": "string",
            "bytes": b"test",
            "set": {"test", "test2"},
            "time": datetime.now(),
        },
    )

    class MyUnsupportedType:
        def __init__(self, data: str) -> None:
            self.data = data

    logger.info("testing types", extra={"random": MyUnsupportedType("test")})
    out, err = capsys.readouterr()
    assert out == ""
    assert "TypeError: Object of type MyUnsupportedType is not JSON serializable" in err


def test_version() -> None:
    assert __version__ is not None
