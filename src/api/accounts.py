from fastapi import APIRouter, Depends, Query

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
