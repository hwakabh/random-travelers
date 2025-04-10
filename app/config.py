from pydantic_settings import BaseSettings
import os
import re


class AppSettings(BaseSettings):
    # BaseSettings of pydantic-settings will read environmental variables first,
    # and if they are not provided, will set default values below.
    MYSQL_HOST: str = re.split('[:@/]', os.environ.get('JAWSDB_URL'))[5]
    MYSQL_USER: str = re.split('[:@/]', os.environ.get('JAWSDB_URL'))[3]
    MYSQL_PASSWORD: str = re.split('[:@/]', os.environ.get('JAWSDB_URL'))[4]
    MYSQL_DATABASE: str = re.split('[:@/]', os.environ.get('JAWSDB_URL'))[7]
    MYSQL_PORT: str = re.split('[:@/]', os.environ.get('JAWSDB_URL'))[6]

    GOOGLE_MAPS_API_KEY: str = ''


app_settings = AppSettings()
