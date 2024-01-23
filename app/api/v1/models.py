from sqlalchemy import Column, String, Integer, Float

from app.database import Base


class Airport(Base):
    __tablename__ = 'airport'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(74))
    city: str = Column(String(35))
    country: str = Column(String(34))
    IATA: str = Column(String(3))
    ICAO: str = Column(String(4))
    latitude: float = Column(Float)
    longitude: float = Column(Float)
    altitude: int = Column(Integer)
    tz_offset: float = Column(Float)
    DST: str = Column(String(1))
    tz_dbtime: str = Column(String(32))
    types: str = Column(String(13))
    datasource: str = Column(String(13))
