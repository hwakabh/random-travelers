from sqlalchemy import Column, String, Integer, Float

from app.database import Base


class Airport(Base):
    # Schema: https://openflights.org/data.php#airport
    # Source: https://github.com/jpatokal/openflights/blob/master/data/airports.dat
    __tablename__ = 'airport'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(74))
    city: str = Column(String(35))
    country: str = Column(String(34))
    IATA: str = Column(String(3))
    ICAO: str = Column(String(4))
    latitude: float = Column(Float)
    longitude: float = Column(Float)
    altitude: int = Column(Integer)
    tz_offset: float = Column(String(256))  # generally int values like 10, but there is the case with string value `\\N`
    DST: str = Column(String(3))  # generally DST value is: E,A,S,O,Z,N,U but there is the case `\\N`
    tz_dbtime: str = Column(String(32))
    types: str = Column(String(13))
    datasource: str = Column(String(13))
