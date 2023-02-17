import logging
import pathlib
import tomllib
from dataclasses import dataclass

__all__ = (
    'AppConfig',
    'LoggingConfig',
    'DodoISAPICredentialsConfig',
    'ExternalAPIConfig',
    'Config',
    'load_config',
    'setup_logging',
    'config',
)

CONFIG_FILE_PATH = pathlib.Path(__file__).parent.parent / 'config.toml'


@dataclass(frozen=True, slots=True)
class DatabaseConfig:
    url: str


@dataclass(frozen=True, slots=True)
class AppConfig:
    debug: bool
    secret_key: str
    host: str
    port: int


@dataclass(frozen=True, slots=True)
class LoggingConfig:
    level: str
    logfile_path: str


@dataclass(frozen=True, slots=True)
class ExternalAPIConfig:
    auth_service_base_url: str


@dataclass(frozen=True, slots=True)
class DodoISAPICredentialsConfig:
    client_id: str
    client_secret: str


@dataclass(frozen=True, slots=True)
class Config:
    database: DatabaseConfig
    app: AppConfig
    logging: LoggingConfig
    external_api: ExternalAPIConfig
    dodo_is_api_credentials: DodoISAPICredentialsConfig


def load_config(config_file_path: str | pathlib.Path) -> Config:
    with open(config_file_path, 'rb') as file:
        config = tomllib.load(file)
    return Config(
        database=DatabaseConfig(
            url=config['database']['url'],
        ),
        app=AppConfig(
            debug=config['app']['debug'],
            secret_key=config['app']['secret_key'],
            host=config['app']['host'],
            port=config['app']['port'],
        ),
        logging=LoggingConfig(
            level=config['logging']['level'],
            logfile_path=config['logging']['logfile_path'],
        ),
        external_api=ExternalAPIConfig(
            auth_service_base_url=config['external_api']['auth_service_base_url'],
        ),
        dodo_is_api_credentials=DodoISAPICredentialsConfig(
            client_id=config['dodo_is_api_credentials']['client_id'],
            client_secret=config['dodo_is_api_credentials']['client_secret'],
        ),
    )


def setup_logging(logging_config: LoggingConfig) -> None:
    logging.basicConfig(filename=logging_config.logfile_path, level=logging_config.level)


config = load_config(CONFIG_FILE_PATH)
