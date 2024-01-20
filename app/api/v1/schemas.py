from pydantic import BaseModel


class TranslateReqBody(BaseModel):
    data: str
