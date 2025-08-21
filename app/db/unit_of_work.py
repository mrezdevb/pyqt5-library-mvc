from app.db.db import SessionLocal
from app.repositories.book_repository import BookRepository
from app.repositories.member_repository import MemberRepository
from app.repositories.loan_repository import LoanRepository

class UnitOfWork:
	def __init__(self, SessionLocal):
		self.session = SessionLocal()
		self.book_repo = BookRepository(self.session)
		self.member_repo = MemberRepository(self.session)
		self.loan_repo = LoanRepository(self.session)

	def commit(self):
		try:
			self.session.commit()
		except:
			self.session.rollback()
			raise
	
	def rollback(self):
		self.session.rollback()

	def close(self):
		self.session.close()

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		if exc_type:
			self.rollback()
		else:
			self.commit()
		self.close()