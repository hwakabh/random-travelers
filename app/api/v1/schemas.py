from pydantic import BaseModel


class RootResponseBase(BaseModel):
    pass


class RootResponse(RootResponseBase):
    path: str
    detail: str


class TranslateReqBody(BaseModel):
    country: str


class AirportBase(BaseModel):
    pass


class Airport(AirportBase):
    id: int

    class Config:
        orm_mode = True


class SearchRequestBody(BaseModel):
    time_limit: int
    expense_limit: int
    current_lat: float
    current_lng: float
