from fastapi import APIRouter

router = APIRouter(tags=['Healthcheck'])


@router.get('/ping/', status_code=200)
def ping():
    return 'pong'
