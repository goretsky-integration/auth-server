import datetime

from sqlalchemy import DateTime, func, String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base


class AccountCredentials:
    account_name: Mapped[str] = mapped_column(String(64), primary_key=True, nullable=False)
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
    )
    __mapper_args__ = {"eager_defaults": True}


class AccountTokens(AccountCredentials, Base):
    __tablename__ = 'account_tokens'

    access_token: Mapped[str] = mapped_column(nullable=False)
    refresh_token: Mapped[str] = mapped_column(nullable=False)


class AccountCookies(Base, AccountCredentials):
    __tablename__ = 'account_cookies'

    cookies: Mapped[dict] = mapped_column(JSON, nullable=False)
