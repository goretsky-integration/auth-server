import uvicorn

from app import get_application
from config import config

app = get_application()


def main():
    uvicorn.run(
        'main:app',
        host=config.app.host,
        port=config.app.port,
    )


if __name__ == '__main__':
    main()
