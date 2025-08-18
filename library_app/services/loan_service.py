from library_app.models.book import Book
from library_app.models.member import Member
from library_app.models.loan import Loan
from library_app.utils.logger import get_logger
from datetime import datetime, timezone
import os

logger = get_logger('LoanService')

class LoanService:
	def __init__(self, session):
		self.db = session

	def loan_book(self, member_id, isbn):
		max_borrow_limit = int(os.getenv('MAX_BORROW_LIMIT', 3))
		book = self.db.query(Book).filter(Book.isbn == isbn).first()
		member = self.db.query(Member).filter(Member.member_id == member_id).first()
		active_loans_book = self.db.query(Loan).filter(
			Loan.member_id == member_id, Loan.returned == False
		).count()
		

		if not member:
			msg = f'Member ID {member_id} not found'
			logger.error(msg)
			return False, msg

		if not book:
			msg = f'Book with ISBN {isbn} not found'
			logger.error(msg)
			return False, msg

		if book.is_borrowed:
			msg = f'Book with ISBN {isbn} is already borrowed.'
			logger.warning(msg)
			return False, msg

		if active_loans_book >= max_borrow_limit:
			msg = f'This member already has {max_borrow_limit} borrowed books.'
			logger.warning(msg)
			return False, msg

		new_loan = Loan(
			member_id=str(member.member_id),
			isbn=str(book.isbn),
			loan_date=datetime.now(timezone.utc),
		)
		book.is_borrowed = True
		self.db.add(new_loan)
		return True, f'Book {book.title} loaned to {member.name}.'


	def return_book(self, member_id, isbn):
		member = self.db.query(Member).filter(Member.member_id == member_id).first()
		book = self.db.query(Book).filter(Book.isbn == isbn).first()
		
		if not member:
			msg = f'Member ID {member_id} not found'
			logger.error(msg)
			return False, msg
		if not book:
			msg = f'Book ISBN {isbn} not found'
			logger.error(msg)
			return False, msg

		loan = self.db.query(Loan).filter(
			Loan.isbn == isbn,
			Loan.member_id == member_id,
			Loan.returned == False
		).first()
		if not loan:
			msg = f'Book {isbn} was not loaned'
			logger.warning(msg)
			return False, msg
		loan.returned = True
		book.is_borrowed = False
		return True, f'Book {isbn} returned by member {member_id}'


