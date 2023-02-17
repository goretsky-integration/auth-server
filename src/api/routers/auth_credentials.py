from fastapi import APIRouter

router = APIRouter(prefix='/auth')


@router.get('/token/')
def get_token():
    pass


@router.patch('/token/')
def update_token():
    pass


@router.get('/cookies/')
def get_cookies():
    pass


@router.patch('/cookies/')
def update_cookies():
    pass
