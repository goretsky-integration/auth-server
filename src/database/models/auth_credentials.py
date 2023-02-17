import datetime

from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from sqlalchemy.dialects.postgresql import JSON

from database.models.accounts import Account
from database.models.base import Base


class AccountCredentials:
    id: Mapped[int] = mapped_column(primary_key=True)
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    )
    account_id: Mapped[int] = mapped_column(ForeignKey('accounts.id'), nullable=False, unique=True)

    @declared_attr
    def account(self) -> Mapped[Account]:
        return relationship('Account')

    __mapper_args__ = {"eager_defaults": True}


class AccountTokens(AccountCredentials, Base):
    __tablename__ = 'account_tokens'

    access_token: Mapped[str] = mapped_column(nullable=False)
    refresh_token: Mapped[str] = mapped_column(nullable=False)


class AccountCookies(Base, AccountCredentials):
    __tablename__ = 'account_cookies'

    cookies: Mapped[dict] = mapped_column(JSON, nullable=False)
