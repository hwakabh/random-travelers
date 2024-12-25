# from datetime import datetime

from sqlalchemy import create_engine, Column, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import app_settings


# dialect for using with mysql-connector-python
ENGINE_URL = "mysql+mysqlconnector://{user}:{password}@{host}:{port}".format(
    user=app_settings.MYSQL_USER,
    password=app_settings.MYSQL_PASSWORD,
    host=app_settings.MYSQL_HOST,
    port=app_settings.MYSQL_PORT,
)

# Create database for first migrations
with create_engine(ENGINE_URL).connect() as conn:
    conn.execute(text(f'CREATE DATABASE IF NOT EXISTS {app_settings.MYSQL_DATABASE}'))

# Configurations for returing database instances
engine = create_engine(
    ENGINE_URL + '/' + app_settings.MYSQL_DATABASE,
    echo=False,
)


def get_db():
    db = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

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
