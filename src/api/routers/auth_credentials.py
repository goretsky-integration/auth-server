from fastapi import APIRouter, Query, Body

from api import schemas

router = APIRouter(prefix='/auth', tags=['Auth credentials'])


@router.get('/token/')
def get_token(
        account_name: schemas.AccountName = Query(),
) -> schemas.AccountTokens:
    pass


@router.patch('/token/')
def update_token(
        tokens: schemas.AccountTokens = Body(),
):
    pass


@router.get('/cookies/')
def get_cookies(
        account_name: schemas.AccountName = Query(),
) -> schemas.AccountCookies:
    pass


@router.patch('/cookies/')
def update_cookies(
        cookies: schemas.AccountCookies = Body(),
):
    pass
