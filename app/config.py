from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    # BaseSettings of pydantic-settings will read environmental variables first,
    # and if they are not provided, will set default values below.
    MYSQL_HOST: str = 'localhost'
    MYSQL_USER: str = 'root'
    MYSQL_PASSWORD: str = 'root'
    MYSQL_DATABASE: str = 'rt'


app = AppSettings()
