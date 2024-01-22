from pydantic import BaseModel


class TranslateReqBody(BaseModel):
    country: str


class AirportBase(BaseModel):
    pass


class Airport(AirportBase):
    id: int

    class Config:
        orm_mode = True
