from fastapi import APIRouter, Depends, Query, Response, status

from api import schemas
from api.dependencies import get_accounts_repository
from repositories import AccountRepository

router = APIRouter(prefix='/accounts')


@router.get('/')
def get_all_accounts(
        limit: int = Query(default=100),
        skip: int = Query(default=0),
        accounts: AccountRepository = Depends(get_accounts_repository),
) -> list[schemas.Account]:
    return accounts.get_all(limit=limit, skip=skip)


@router.post('/')
def create_account(
        account: schemas.Account,
        accounts: AccountRepository = Depends(get_accounts_repository),
):
    accounts.create(name=account.name, login=account.login, password=account.password)
    return Response(status_code=status.HTTP_201_CREATED)
