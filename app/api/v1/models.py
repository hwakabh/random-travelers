from sqlalchemy import Column, String, Integer

from app.database import Base


class Airport(Base):
    __tablename__ = 'airport'

    id: int = Column(Integer, primary_key=True)
