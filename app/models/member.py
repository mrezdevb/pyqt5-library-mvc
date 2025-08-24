from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.loan import Loan

from .base import Base


class Member(Base):
    __tablename__ = "members"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    member_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    loans: Mapped[list[Loan]] = relationship(
        "Loan", back_populates="member", cascade="all, delete"
    )

    def __repr__(self) -> str:
        return f'<Member(name="{self.name}"), member_id="{self.member_id}")>'
