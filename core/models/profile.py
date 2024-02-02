from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

# Что-бы небыло циклического импорта, импортируем User только при проверки типов
if TYPE_CHECKING:
    from .user import User


class Profile(Base):
    __tablename__ = "profiles"

    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    bio: Mapped[str | None]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
