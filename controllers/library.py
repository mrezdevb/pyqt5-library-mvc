from models.book import Book
from models.member import Member
from utils.logger import get_logger
logger = get_logger("LibraryManagement")

class LibraryManagement:

	def __init__(self):
		self.books = []
		self.members = []
		self.loans = {}



	def add_book(self, title, author, isbn):
		if any(book.isbn == isbn for book in self.books):
			msg = 'This book is already available.'
			logger.warning(msg)
			return False, msg
		self.books.append(Book(title, author, isbn))
		return True, 'This book successfully added'
	


	def remove_book(self, isbn):
		for i, book in enumerate(self.books):
			if book.isbn == isbn:
				removed = self.books.pop(i)
				msg = f'Book removed {removed}'
				logger.info(msg)
				return True, msg
		msg = f'Book with ISBN {isbn} not found.'
		logger.warning(msg)
		return False, msg
	


	def add_member(self, name, member_id):
		if any(member.member_id == member_id for member in self.members):
			msg = 'This member is already available.'
			logger.warning(msg)
			return False, msg
		self.members.append(Member(name, member_id))
		return True, 'This member successfully added'
	


	def remove_member(self, member_id):
		for i, member in enumerate(self.members):
			if member.member_id == member_id:
				removed = self.members.pop(i)
				msg = f'Member removed {removed}'
				logger.info(msg)
				return True, msg
		msg = f'Member with member ID {member_id} not found.'
		logger.warning(msg)
		return False, msg
	


	def show_books(self):
		if not self.books:
			logger.info('No books available.')
			return 
		return self.books
	


	def show_members(self):
		if not self.members:
			logger.info('No members available.')
			return
		return self.members





	def loan_book(self, member_id, isbn):
		member = next((member for member in self.members if member.member_id == member_id), None)
		book = next((book for book in self.books if book.isbn == isbn), None)
		if not member:
			msg = f'Member ID {member_id} not found'
			logger.error(msg)
			return False, msg
		if not book:
			msg = f'Book with ISBN {isbn} not found'
			logger.error(msg)
			return False, msg
		if not book.is_barrowed:
			book.is_barrowed = True
			self.loans[isbn] = member
			msg = f'Book {isbn} loaned to member {member_id}'
			logger.info(msg)
			return True, msg
		msg = f'Book {isbn} is already loaned out'
		logger.warning(msg)
		return False, msg
	



	def return_book(self, member_id, isbn):
		member = next((member for member in self.members if member.member_id == member_id), None)
		book = next((book for book in self.books if book.isbn == isbn), None)
		if not member:
			msg = f'Member ID {member_id} not found'
			logger.error(msg)
			return False, msg
		if not book:
			msg = f'Book ISBN {isbn} not found'
			logger.error(msg)
			return False, msg
		if not book.is_barrowed:
			msg = f'Book {isbn} was not loaned.'
			logger.warning(msg)
			return False, msg
		book.is_barrowed = False
		self.loans.pop(isbn, None)
		msg = f'Book {isbn} returned by member {member_id}'
		logger.info(msg)
		return True, msg
