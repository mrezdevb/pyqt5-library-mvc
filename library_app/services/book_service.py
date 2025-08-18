from library_app.models.book import Book
from library_app.utils.logger import get_logger

logger = get_logger('BookService')

class BookService:
	def __init__(self, db_session):
		self.db = db_session
	
	def add_book(self, title: str, author: str, isbn: str):
		existing_book = self.db.query(Book).filter(Book.isbn == isbn).first()
		if existing_book:
			msg = 'This book is already available.'
			logger.warning(msg)
			return False, msg
		new_book = Book(title=title, author=author, isbn=isbn)
		self.db.add(new_book)
		return True, 'This book successfully added'

	def remove_book(self, isbn: str):
		book = self.db.query(Book).filter(Book.isbn == isbn).first()
		if book:
			self.db.delete(book)
			msg = f'Book with ISBN {isbn} removed'
			logger.info(msg)
			return True, msg
		else:
			msg = f'Book with ISBN {isbn} not found'
			logger.warning(msg)
			return False, msg

	def show_books(self, filter_option):
		if filter_option == 'All Books':
			books = self.db.query(Book).all()
		else:
			books = self.db.query(Book).filter(Book.is_borrowed == False).all()
		if not books:
			logger.info('No books available.')
			return []
		return books

	def search_books(self, keyword, filter_option):
		base_query = self.db.query(Book).filter(
			Book.title.ilike(f'%{keyword}%')|
			Book.author.ilike(f'%{keyword}%')|
			Book.isbn.ilike(f'%{keyword}%')
			)
		all_results = base_query.all()
		
		if not all_results:
			msg = f'No books found matching "{keyword}".'
			logger.info(msg)
			return [], 'not found'

		if filter_option != 'All Books':
			available_books = [b for b in all_results if not b.is_borrowed]
			if not available_books:
				msg = f'Books matching "{keyword}" are borrowed.'
				logger.info(msg)
				return [], 'borrowed'
			return available_books, 'ok'
		return all_results, 'ok'
