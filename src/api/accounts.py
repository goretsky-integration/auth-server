from fastapi import APIRouter

from api import schemas

router = APIRouter(prefix='/accounts')


@router.get('/')
def get_all_accounts() -> list[schemas.Account]:
    pass
