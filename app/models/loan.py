from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Loan(Base):
    __tablename__ = "loans"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    member_id: Mapped[str] = mapped_column(
        String, ForeignKey("members.member_id"), nullable=False
    )
    isbn: Mapped[str] = mapped_column(String, ForeignKey("books.isbn"), nullable=False)
    loan_date: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    returned: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    member = relationship("Member", back_populates="loans")
    book = relationship("Book", back_populates="loans")
