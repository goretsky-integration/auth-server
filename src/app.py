from fastapi import FastAPI

import api.routers
from api.errors import include_exception_handlers
from database.engine import engine
from database.models.base import Base

__all__ = ('get_application',)


def on_startup():
    Base.metadata.create_all(engine)


def get_application() -> FastAPI:
    app = FastAPI()
    app.add_event_handler('startup', on_startup)
    app.include_router(api.routers.accounts.router)
    app.include_router(api.routers.auth_credentials.router)
    app.include_router(api.routers.healthcheck.router)
    include_exception_handlers(app)
    return app
