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


class SearchResultResponseBody(BaseModel):
    dest_country: str
    dest_city: str
    dest_iata: str
    dest_airport: str
    dest_lat: float
    dest_lng: float
    tran_country: str
    tran_city: str
    tran_iata: str
    tran_airport: str
    tran_lat: float
    tran_lng: float

    class Config:
        orm_mode = True
