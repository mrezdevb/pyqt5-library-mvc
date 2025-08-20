from app.models.book import Book
from app.db.db import SessionLocal
from app.repositories.book_repository import BookRepository
from app.observability.logger import get_logger
from app.observability.logger_helpers import log_json


logger = get_logger('BookService')


class BookService:
	def __init__(self, db_session):
		self.book_repo = BookRepository(db_session)


	def _log(self, level, action, msg, **kwargs):

		log_json(logger, level, action, msg=msg, **kwargs)



	def add_book(self, title, author, isbn):
		try:
			self._log("info", "BOOK_ADD_START",
					msg=f'Attempting to add book "{title}" (ISBN {isbn})',
					title=title, author=author, isbn=isbn)

			existing_book = self.book_repo.query_by_isbn(isbn).first()
			if existing_book:
				msg = f'Book with ISBN {isbn} already exists.'
				self._log("warning", "BOOK_ADD_EXISTS",
						msg=msg, isbn=isbn, title=existing_book.title)
				return False, msg

			self._log("info", "BOOK_ADD_VALID",
					msg=f'Book "{title}" with ISBN {isbn} is valid for creation.',
					title=title, author=author, isbn=isbn)

			new_book = Book(title=title, author=author, isbn=isbn)

			self._log("debug", "BOOK_ADD_PENDING_COMMIT",
					msg=f'Book "{title}" (ISBN {isbn}) pending commit.',
					title=title, author=author, isbn=isbn)

			self.book_repo.add(new_book)

			msg = f'Book "{title}" (ISBN {isbn}) successfully added.'
			self._log("info", "BOOK_ADD_SUCCESS",
					msg=msg, title=title, author=author, isbn=isbn)

			return True, msg

		except Exception as e:
			self._log("exception", "BOOK_ADD_ERROR",
					msg=f'Error while adding book "{title}" (ISBN {isbn}): {str(e)}',
					title=title, author=author, isbn=isbn, error=str(e))
			raise


	def remove_book(self, isbn):
		try:
			self._log("info", "BOOK_REMOVE_START",
					msg=f'Attempting to remove book with ISBN {isbn}',
					isbn=isbn)

			book = self.book_repo.query_by_isbn(isbn).first()
			if not book:
				msg = f'Book with ISBN {isbn} not found.'
				self._log("warning", "BOOK_REMOVE_NOT_FOUND",
						msg=msg, isbn=isbn)
				return False, msg

			self._log("info", "BOOK_REMOVE_FOUND",
					msg=f'Book "{book.title}" (ISBN {isbn}) found.',
					title=book.title, isbn=isbn)

			self._log("debug", "BOOK_REMOVE_PENDING_DELETE",
					msg=f'Book "{book.title}" (ISBN {isbn}) pending delete.',
					title=book.title, isbn=isbn)

			self.book_repo.remove(book)

			msg = f'Book "{book.title}" (ISBN {isbn}) removed successfully.'
			self._log("info", "BOOK_REMOVE_SUCCESS",
					msg=msg, title=book.title, isbn=isbn)

			return True, msg

		except Exception as e:
			self._log("exception", "BOOK_REMOVE_ERROR",
					msg=f'Error while removing book with ISBN {isbn}: {str(e)}',
					isbn=isbn, error=str(e))
			raise

	def show_books(self, filter_option):
		try:
			self._log("info", "BOOK_FETCH_START",
					msg=f'Retrieving books with filter "{filter_option}"',
					filter_option=filter_option)

			if filter_option == 'All Books':
				self._log("debug", "BOOK_FETCH_ALL",
						msg='Fetching all books from database.')
				books = self.book_repo.query_all().all()
			else:
				self._log("debug", "BOOK_FETCH_AVAILABLE",
						msg='Fetching only available (not borrowed) books.')
				books = self.book_repo.query_by_borrowed_status(False).all()

			self._log("debug", "BOOK_FETCH_QUERY_DONE",
					msg=f'Query executed for filter "{filter_option}".',
					filter_option=filter_option, books_count=len(books))

			if not books:
				self._log("info", "BOOK_FETCH_EMPTY",
						msg=f'No books found with filter "{filter_option}".',
						filter_option=filter_option)
				return []

			self._log("info", "BOOK_FETCH_SUCCESS",
					msg=f'{len(books)} book(s) found with filter "{filter_option}".',
					filter_option=filter_option, books_count=len(books))

			return books

		except Exception as e:
			self._log("exception", "BOOK_FETCH_ERROR",
					msg=f'Error while fetching books with filter "{filter_option}": {str(e)}',
					filter_option=filter_option, error=str(e))
			raise



	def search_books(self, keyword, filter_option):
		try:
			self._log("info", "BOOK_SEARCH_START",
					msg=f'Searching books with keyword "{keyword}" and filter "{filter_option}"',
					keyword=keyword, filter_option=filter_option)

			base_query = self.book_repo.query_by_keyword(keyword)
			self._log("debug", "BOOK_SEARCH_QUERY_BUILD",
					msg="Base query built for searching books.",
					keyword=keyword, filter_option=filter_option)

			all_results = base_query.all()
			self._log("debug", "BOOK_SEARCH_QUERY_EXECUTED",
					msg=f'Query executed, {len(all_results)} result(s) found.',
					keyword=keyword, filter_option=filter_option, results_count=len(all_results))

			if not all_results:
				msg = f'No books found matching "{keyword}".'
				self._log("info", "BOOK_SEARCH_EMPTY",
						msg=msg, keyword=keyword, filter_option=filter_option)
				return [], 'not found'

			self._log("debug", "BOOK_SEARCH_RESULTS_FOUND",
					msg=f'{len(all_results)} book(s) matched keyword "{keyword}".',
					keyword=keyword, filter_option=filter_option)

			if filter_option != 'All Books':

				self._log("debug", "BOOK_SEARCH_FILTER_APPLIED",
						msg="Applying availability filter (only not borrowed).",
						keyword=keyword, filter_option=filter_option)
				available_books = self.book_repo.query_available_books(keyword).all()

				if not available_books:
					msg = f'Books matching "{keyword}" are borrowed.'
					self._log("info", "BOOK_SEARCH_BORROWED",
							msg=msg, keyword=keyword, filter_option=filter_option)
					return [], 'borrowed'

				self._log("info", "BOOK_SEARCH_AVAILABLE_SUCCESS",
						msg=f'{len(available_books)} available book(s) found for keyword "{keyword}".',
						keyword=keyword, filter_option=filter_option, results_count=len(available_books))
				return available_books, 'ok'

			self._log("info", "BOOK_SEARCH_SUCCESS",
					msg=f'{len(all_results)} book(s) found for keyword "{keyword}" with filter "All Books".',
					keyword=keyword, filter_option=filter_option, results_count=len(all_results))
			return all_results, 'ok'

		except Exception as e:
			self._log("exception", "BOOK_SEARCH_ERROR",
					msg=f'Error while searching books with keyword "{keyword}" and filter "{filter_option}": {str(e)}',
					keyword=keyword, filter_option=filter_option, error=str(e))
			raise
