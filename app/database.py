# from datetime import datetime
from sqlalchemy import create_engine, Column, DateTime, text
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import app_settings
from app.api.v1 import models
from app.api.v1.helpers import fetch_airport_data


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
    session_local = db()

    try:
        yield session_local
    finally:
        session_local.close()


def insert_fixtures() -> bool:
    try:
        # TODO: make DRY with database.py
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()

        if s.query(models.Airport).count() != 0:
            print('Initiated, fixture data already loaded.')
            return True

        data: list = fetch_airport_data()
        if data == []:
            print('Failed to fetch raw-data from remote')
            return False

        for i in data:
            record = models.Airport(**{
                'id' : i[0],
                'name': i[1],
                'city': i[2],
                'country': i[3],
                'IATA': i[4].replace('\"', ''),
                'ICAO': i[5].replace('\"', ''),
                'latitude': i[6],
                'longitude': i[7],
                'altitude': i[8],
                'tz_offset': i[9],
                'DST': i[10].replace('\"', ''),
                'tz_dbtime': i[11],
                'types': i[12],
                'datasource': i[13],
            })
            s.add(record)
        s.commit()

        print(f'Loaded {len(data)} lines into MySQL')

    except Exception as e:
        print(f'Error on inserting fixtures: {e}')
        s.rollback()
        return False
    finally:
        s.close()
        return True


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
#
# # when used, the child class in models.py should be looked like:
# class Airport(TimeStampMixin, Base):
# ...

Base = declarative_base()
