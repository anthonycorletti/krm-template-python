import os
import time
from datetime import datetime
from typing import Any, Callable

from fastapi import FastAPI, Request

from krm_template_python import __version__
from krm_template_python.logger import logger
from krm_template_python.types import HealthcheckResponse

os.environ["TZ"] = "UTC"

#
#   create the api
#
api = FastAPI(title="krm_template_python", version=__version__)


#
#   middleware
#
@api.middleware("http")
async def add_process_time_header(request: Request, call_next: Callable) -> Any:
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


#
#   make a route
#
@api.get("/healthz", response_model=HealthcheckResponse, tags=["health"])
def healthcheck() -> HealthcheckResponse:
    message = "We're on the air."
    time = datetime.now()
    logger.info(msg=message, extra={"version": __version__, "time": time})
    return HealthcheckResponse(
        message=message, version=__version__, time=datetime.now()
    )
