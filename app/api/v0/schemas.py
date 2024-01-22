from pydantic import BaseModel


class RootResponseBase(BaseModel):
    pass


class RootResponse(RootResponseBase):
    path: str
    detail: str
