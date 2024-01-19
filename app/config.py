from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    MYSQL_HOST: str = 'localhost'
    MYSQL_USER: str = 'root'
    MYSQL_PASSWORD: str = 'root'
    MYSQL_DATABASE: str = 'rt'


app = AppSettings()
