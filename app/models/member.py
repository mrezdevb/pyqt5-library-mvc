from sqlalchemy import Column, Integer, String
from .base import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.models.loan import Loan
from app.models.book import Book
class Member(Base):
	__tablename__ = 'members'
	id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
	name: Mapped[str] = mapped_column(String, nullable=False)
	member_id: Mapped[str] = mapped_column(String,unique=True,  nullable=False)
	loans: Mapped[list[Loan]] = relationship('Loan', back_populates='member', cascade='all, delete')
	
	def __repr__(self) -> str:
		return f'<Member(name="{self.name}"), member_id="{self.member_id}")>'

