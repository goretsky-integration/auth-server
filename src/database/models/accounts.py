from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base

__all__ = ('Account',)


class Account(Base):
    __tablename__ = 'accounts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    login: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    def __str__(self):
        return f'<Account {self.name}>'
