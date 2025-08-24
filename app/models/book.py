from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.loan import Loan

from .base import Base


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    isbn: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    is_borrowed: Mapped[bool] = mapped_column(Boolean, default=False)
    loans: Mapped[list["Loan"]] = relationship(
        "Loan", back_populates="book", cascade="all, delete"
    )

    def __repr__(self) -> str:
        return (
            f'<Book(title="{self.title}", author="{self.author}", isbn="{self.isbn}")>'
        )
