from datetime import datetime

from pydantic import BaseModel, StrictStr


class HealthcheckResponse(BaseModel):
    message: StrictStr
    version: StrictStr
    time: datetime
