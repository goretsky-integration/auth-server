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
)


@dataclass(frozen=True, slots=True)
class AppConfig:
    debug: bool
    secret_key: str


@dataclass(frozen=True, slots=True)
class LoggingConfig:
    level: str
    logfile_path: str


@dataclass(frozen=True, slots=True)
class ExternalAPIConfig:
    auth_service_base_url: str
    database_service_base_url: str


@dataclass(frozen=True, slots=True)
class DodoISAPICredentialsConfig:
    client_id: str
    client_secret: str


@dataclass(frozen=True, slots=True)
class Config:
    app: AppConfig
    logging: LoggingConfig
    external_api: ExternalAPIConfig
    dodo_is_api_credentials: DodoISAPICredentialsConfig


def load_config(config_file_path: str | pathlib.Path) -> Config:
    with open(config_file_path, 'rb') as file:
        config = tomllib.load(file)
    return Config(
        app=AppConfig(
            debug=config['app']['debug'],
            secret_key=config['app']['secret_key'],
        ),
        logging=LoggingConfig(
            level=config['logging']['level'],
            logfile_path=config['logging']['logfile_path'],
        ),
        external_api=ExternalAPIConfig(
            auth_service_base_url=config['external_api']['auth_service_base_url'],
            database_service_base_url=config['external_api']['database_service_base_url'],
        ),
        dodo_is_api_credentials=DodoISAPICredentialsConfig(
            client_id=config['dodo_is_api_credentials']['client_id'],
            client_secret=config['dodo_is_api_credentials']['client_secret'],
        ),
    )


def setup_logging(logging_config: LoggingConfig) -> None:
    logging.basicConfig(filename=logging_config.logfile_path, level=logging_config.level)
