from pydantic import BaseModel


class TranslateReqBody(BaseModel):
    country: str
