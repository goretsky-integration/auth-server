from fastapi import FastAPI

import api.routers.accounts

__all__ = ('get_application',)


def get_application() -> FastAPI:
    app = FastAPI()
    app.include_router(api.routers.accounts.router)
    return app
