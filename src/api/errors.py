from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

import exceptions

__all__ = ('include_exception_handlers',)


def on_already_exists_exception(request, exc):
    return JSONResponse({'detail': str(exc)}, status_code=status.HTTP_409_CONFLICT)


def include_exception_handlers(app: FastAPI):
    app.add_exception_handler(
        exceptions.AlreadyExistsInDatabase,
        on_already_exists_exception,
    )
