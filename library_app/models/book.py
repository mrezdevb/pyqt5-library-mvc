from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class Book(Base):
	__tablename__ = 'books'
	id = Column(Integer, primary_key=True, index=True)
	title = Column(String, nullable=False)
	author = Column(String, nullable=False)
	isbn = Column(String, unique=True, nullable=False)
	is_borrowed = Column(Boolean, default=False)
	loans = relationship('Loan', back_populates='book', cascade='all, delete')

	def __repr__(self):
		return f'<Book(title="{self.title}", author="{self.author}", isbn="{self.isbn}")>'


