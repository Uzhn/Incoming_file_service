from datetime import date

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base_class import Base


class Flight(Base):
    """Model Flight."""

    file_name: Mapped[str] = mapped_column(sa.String(length=120), nullable=False)
    fit: Mapped[int] = mapped_column(sa.Integer, nullable=False)
    dep_date: Mapped[date] = mapped_column(sa.Date(), nullable=False)
    dep: Mapped[str] = mapped_column(sa.String(length=120), nullable=False)

    def __str__(self):
        return f"Flight(file_name={self.file_name!r})"

    def __repr__(self) -> str:
        return str(self)
