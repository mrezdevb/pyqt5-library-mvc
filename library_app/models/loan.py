from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean, String
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime, timezone


class Loan(Base):
	__tablename__ = 'loans'
	id = Column(Integer, primary_key=True, index=True)
	member_id = Column(String, ForeignKey('members.member_id'), nullable=False)
	isbn = Column(String, ForeignKey('books.isbn'), nullable=False)
	loan_date = Column(DateTime, default=datetime.now(timezone.utc))
	returned = Column(Boolean, default=False, nullable=False)

	member = relationship('Member', back_populates='loans')
	book = relationship('Book', back_populates='loans')

