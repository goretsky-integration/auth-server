from fastapi import APIRouter, Query, Body, Depends, status, Response

from api import schemas, dependencies
from repositories import AccountTokensRepository, AccountCookiesRepository

router = APIRouter(prefix='/auth', tags=['Auth credentials'])


@router.get('/token/', response_model=schemas.AccountTokens)
def get_token(
        account_name: schemas.AccountName = Query(),
        accounts_tokens: AccountTokensRepository = Depends(dependencies.get_account_tokens_repository),
):
    return accounts_tokens.get_by_account_name(account_name)


@router.patch('/token/')
def update_token(
        tokens: schemas.AccountTokens = Body(),
        accounts_tokens: AccountTokensRepository = Depends(dependencies.get_account_tokens_repository),
):
    accounts_tokens.update(
        account_name=tokens.account_name,
        access_token=tokens.access_token,
        refresh_token=tokens.refresh_token,
    )
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get('/cookies/', response_model=schemas.AccountCookies)
def get_cookies(
        account_name: schemas.AccountName = Query(),
        accounts_cookies: AccountCookiesRepository = Depends(dependencies.get_account_cookies_repository),
):
    return accounts_cookies.get_by_account_name(account_name)


@router.patch('/cookies/')
def update_cookies(
        account_cookies: schemas.AccountCookies = Body(),
        accounts_cookies: AccountCookiesRepository = Depends(dependencies.get_account_cookies_repository),
):
    accounts_cookies.update(account_name=account_cookies.account_name, cookies=account_cookies.cookies)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
