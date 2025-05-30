
from pydantic import BaseModel, ConfigDict


class Request(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )


class Response(BaseModel):
    pass
