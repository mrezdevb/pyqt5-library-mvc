from app.models.book import Book
from app.models.member import Member
from app.models.loan import Loan
from app.observability.logger import get_logger
from app.observability.logger_helpers import log_json
from datetime import datetime, timezone
import os


logger = get_logger('LoanService')


class LoanService:


	def __init__(self, session):
		self.db = session


	def _log(self, level, action, msg, **kwargs):

		log_json(logger, level, action, msg=msg, **kwargs)



	def loan_book(self, member_id, isbn):
		try:

			self._log("info", "LOAN_BOOK_START",
					msg=f'Attempting to loan book {isbn} to member {member_id}',
					member_id=member_id, isbn=isbn)

			max_borrow_limit = int(os.getenv('MAX_BORROW_LIMIT', 3))
			
			self._log("debug", "CONFIG_BORROW_LIMIT",
					msg=f'Max borrow limit is {max_borrow_limit}',
					limit=max_borrow_limit)

			book = self.db.query(Book).filter(Book.isbn == isbn).first()
			
			if not book:
				msg = f'Book with ISBN {isbn} not found'
				self._log("warning", "BOOK_NOT_FOUND", msg=msg, isbn=isbn)
				return False, msg
			
			self._log("info", "BOOK_FOUND",
					msg=f'Book "{book.title}" with ISBN {isbn} found.',
					isbn=isbn, title=book.title)

			member = self.db.query(Member).filter(Member.member_id == member_id).first()
			
			if not member:
				msg = f'Member ID {member_id} not found'
				self._log("warning", "MEMBER_NOT_FOUND", msg=msg, member_id=member_id)
				return False, msg
			
			self._log("info", "MEMBER_FOUND",
					msg=f'Member "{member.name}" with ID {member_id} found.',
					member_id=member_id, name=member.name)

			active_loans_book = self.db.query(Loan).filter(
				Loan.member_id == member_id, Loan.returned == False
			).count()
			
			self._log("debug", "ACTIVE_LOANS_COUNT",
					msg=f'Member {member_id} currently has {active_loans_book} active loans.',
					member_id=member_id, active_loans=active_loans_book)

			if book.is_borrowed:
				msg = f'Book with ISBN {isbn} is already borrowed.'
				self._log("warning", "BOOK_ALREADY_BORROWED", msg=msg, isbn=isbn)
				return False, msg

			if active_loans_book >= max_borrow_limit:
				msg = f'This member already has {max_borrow_limit} borrowed books.'
	
				self._log("warning", "BORROW_LIMIT_EXCEEDED", msg=msg,
						member_id=member_id, limit=max_borrow_limit)
	
				return False, msg

			new_loan = Loan(
				member_id=member.member_id,
				isbn=book.isbn,
				loan_date=datetime.now(timezone.utc),
			)
	
			self._log("debug", "LOAN_PENDING_COMMIT",
					msg=f'Loan for book {isbn} pending commit.',
					member_id=member_id, isbn=isbn)

			book.is_borrowed = True
			self.db.add(new_loan)

			msg = f'Book "{book.title}" loaned to {member.name}.'
	
			self._log("info", "LOAN_SUCCESS",
					msg=msg, member_id=member_id, isbn=isbn,
					title=book.title, member_name=member.name)

			return True, msg

		except Exception as e:
	
			self._log("exception", "LOAN_ERROR",
					msg=f'Error while loaning book {isbn} to member {member_id}: {str(e)}',
					member_id=member_id, isbn=isbn, error=str(e))
	
			raise


	def return_book(self, member_id, isbn):
		try:
	
			self._log("info", "RETURN_BOOK_START",
					msg=f'Attempting to return book {isbn} for member {member_id}',
					member_id=member_id, isbn=isbn)

			member = self.db.query(Member).filter(Member.member_id == member_id).first()
	
			if not member:
				msg = f'Member ID {member_id} not found'
				self._log("warning", "MEMBER_NOT_FOUND",
						msg=msg, member_id=member_id)
				return False, msg
	
			self._log("info", "MEMBER_FOUND",
					msg=f'Member "{member.name}" with ID {member_id} found.',
					member_id=member_id, name=member.name)

			book = self.db.query(Book).filter(Book.isbn == isbn).first()
	
			if not book:
				msg = f'Book ISBN {isbn} not found'
				self._log("warning", "BOOK_NOT_FOUND",
						msg=msg, isbn=isbn)
				return False, msg
	
			self._log("info", "BOOK_FOUND",
					msg=f'Book "{book.title}" with ISBN {isbn} found.',
					isbn=isbn, title=book.title)

			loan = self.db.query(Loan).filter(
				Loan.isbn == isbn,
				Loan.member_id == member_id,
				Loan.returned == False
			).first()
	
			if not loan:
				msg = f'Book {isbn} was not loaned by member {member_id}'
				self._log("warning", "LOAN_NOT_FOUND",
						msg=msg, member_id=member_id, isbn=isbn)
				return False, msg
	
			self._log("info", "LOAN_FOUND",
					msg=f'Active loan found for book {isbn} and member {member_id}.',
					loan_id=loan.id, member_id=member_id, isbn=isbn)

			loan.returned = True
	
			book.is_borrowed = False
	
			msg = f'Book "{book.title}" returned by member {member_id}'
	
			self._log("info", "RETURN_BOOK_SUCCESS",
					msg=msg, member_id=member_id, isbn=isbn, title=book.title)

			return True, msg

		except Exception as e:
	
			self._log("exception", "RETURN_BOOK_ERROR",
					msg=f'Error while returning book {isbn} for member {member_id}: {str(e)}',
					member_id=member_id, isbn=isbn, error=str(e))
	
			raise



