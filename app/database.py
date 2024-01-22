from datetime import datetime

from sqlalchemy import create_engine, Column, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import app_settings


# dialect for using with mysql-connector-python
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{dbname}".format(
    user=app_settings.MYSQL_USER,
    password=app_settings.MYSQL_PASSWORD,
    host=app_settings.MYSQL_HOST,
    port=3306,
    dbname=app_settings.MYSQL_DATABASE
)


# Configurations for returing database instances
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=False
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# # Base class definitions for each model
# class TimeStampMixin(object):
#     created_at = Column(
#         DateTime,
#         default=datetime.now,
#         nullable=False,
#         server_default=text("current_timestamp"))
#     updated_at = Column(
#         DateTime,
#         default=datetime.now,
#         nullable=False,
#         server_default=text("current_timestamp"))


Base = declarative_base()
