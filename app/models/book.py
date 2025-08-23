from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base
from app.models.loan import Loan
class Book(Base):
	__tablename__ = 'books'
	id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
	title: Mapped[str] = mapped_column(String, nullable=False)
	author: Mapped[str] = mapped_column(String, nullable=False)
	isbn: Mapped[str] = mapped_column(String, unique=True, nullable=False)
	is_borrowed: Mapped[bool] = mapped_column(Boolean, default=False)
	loans: Mapped[list['Loan']]= relationship('Loan', back_populates='book', cascade='all, delete')

	def __repr__(self) -> str:
		return f'<Book(title="{self.title}", author="{self.author}", isbn="{self.isbn}")>'


