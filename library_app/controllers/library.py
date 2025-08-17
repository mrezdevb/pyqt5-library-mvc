from library_app.models.book import Book
from library_app.models.member import Member
from library_app.models.loan import Loan
from library_app.utils.logger import get_logger
from datetime import datetime, timezone
from dotenv import load_dotenv
from sqlalchemy.orm import joinedload
import os
load_dotenv()

logger = get_logger("LibraryManagement")

class LibraryManagement:

	def __init__(self, db_session):
		self.db = db_session

	

	def add_book(self, title : str, author : str, isbn : str):
		existing_book = self.db.query(Book).filter(Book.isbn == isbn).first()
		if existing_book:
			msg = 'This book is already available.'
			logger.warning(msg)
			return False, msg
		new_book = Book(title=title, author=author, isbn=isbn)
		self.db.add(new_book)
		self.db.commit()
		return True, 'This book successfully added'
	
	def remove_book(self, isbn: str):
		book = self.db.query(Book).filter(Book.isbn == isbn).first()
		if book:
			self.db.delete(book)
			self.db.commit()
			msg = f'Book with ISBN {isbn} removed.'
			logger.info(msg)
			return True, msg
		else:
			msg = f'Book with ISBN {isbn} not found'
			logger.warning(msg)
			return False, msg

	


	def add_member(self, name: str, member_id: str):
		existing_member = self.db.query(Member).filter(Member.member_id == member_id).first()	
		if existing_member:
			msg = 'This member is already available.'
			logger.warning(msg)
			return False, msg
		new_member = Member(name=name, member_id=member_id)
		self.db.add(new_member)
		self.db.commit()
		return True, 'This member successfully added'
	


	def remove_member(self, member_id):
		member = self.db.query(Member).filter(Member.member_id == member_id).first()
		if member:
			self.db.delete(member)
			msg = f'Member with member_id: {member_id} removed'
			logger.info(msg)
			self.db.commit()
			return True, msg
		else:
			msg = f'Member with member_id: {member_id} not found'
			logger.warning(msg)
			return False, msg


	def show_books(self, filter_option: str):
		books = ''
		if filter_option == 'All Books':
			books = self.db.query(Book).all()
		else:
			books = self.db.query(Book).filter(Book.is_borrowed == False).all()
		if not books:
			logger.info('No books available.')
			return []
		return books
		
	def _format_members(self, members):
		result = []
		for member in members:
			borrowed_books = [
					loan.book.title for loan in member.loans if not loan.returned
			]
			result.append({
				'name':member.name,
				'member_id':member.member_id,
				'borrowed_books': ', '.join(borrowed_books) if borrowed_books else '-'
			})
		return result	


	def show_members(self):
		members = self.db.query(Member).options(joinedload(Member.loans).joinedload(Loan.book)).all()
		if not members:
				logger.info('No members available.')
				return []
		return self._format_members(members)





	def loan_book(self, member_id: str, isbn: str):
		max_borrow_limit = os.getenv('MAX_BORROW_LIMIT')
		book = self.db.query(Book).filter(Book.isbn == isbn).first()
		member = self.db.query(Member).filter(Member.member_id == member_id).first()
		active_loans_book = (self.db.query(Loan).filter(Loan.member_id == member_id, Loan.returned == False).count())
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
		if int(active_loans_book) >= int(max_borrow_limit):
			msg = f'This member already has {max_borrow_limit} borrowed books.'
			logger.warning(msg)
			return False, msg
		new_loan = Loan(member_id = str(member.member_id), isbn = str(book.isbn), loan_date=datetime.now(timezone.utc))
		book.is_borrowed = True
		self.db.add(new_loan)
		self.db.commit()
		
		msg = f'Book {book.title} loaned to {member.name}.'
		logger.info(msg)
		return True, msg



	def return_book(self, member_id: str, isbn: str):
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
		loan= self.db.query(Loan).filter(Loan.isbn == isbn, Loan.member_id == member_id, Loan.returned == False).first()
		if not loan:
			msg = f'Book {isbn} was not loaned.'
			logger.warning(msg)
			return False, msg
		loan.returned = True
		book.is_borrowed = False
		self.db.commit()
		msg = f'Book {isbn} returned by member {member_id}'
		logger.info(msg)
		return True, msg

	def search_books(self, keyword: str, filter_option: str):
		base_query = self.db.query(Book).filter(
			Book.title.ilike(f'%{keyword}%') |
			Book.author.ilike(f'%{keyword}%') |
			Book.isbn.ilike(f'%{keyword}%')
		)

		all_results = base_query.all()
		if not all_results:
			msg = f'No books found matching "{keyword}".'
			logger.info(msg)
			return [], 'not found'

		if filter_option != 'All Books':
			available_books = [book for book in all_results if not book.is_borrowed]
			if not available_books:
				msg = f'Books matching "{keyword}" are borrowed.'
				logger.info(msg)
				return [], 'borrowed'
			return available_books, 'ok'

		return all_results, 'ok'



		

	def search_members(self, keyword: str):
			results = self.db.query(Member).options(joinedload(Member.loans).joinedload(Loan.book)).filter(Member.name.ilike(f'%{keyword}%') | Member.member_id.ilike(f'%{keyword}%')).all()
			if not results:
					logger.info(f'No members found matching "{keyword}".')
					return []
			return self._format_members(results)
