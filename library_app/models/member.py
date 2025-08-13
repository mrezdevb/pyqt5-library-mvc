from sqlalchemy import Column, Integer, String
from .base import Base
from sqlalchemy.orm import relationship
from library_app.models.loan import Loan
from library_app.models.book import Book
class Member(Base):
	__tablename__ = 'members'
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, nullable=False)
	member_id = Column(String,unique=True,  nullable=False)
	loans = relationship('Loan', back_populates='member', cascade='all, delete')
	
	def __repr__(self):
		return f'<Member(name="{self.name}"), member_id="{self.member_id}")>'

