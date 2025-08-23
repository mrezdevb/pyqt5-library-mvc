from app.models.book import Book
from app.db.db import SessionLocal
from sqlalchemy import or_
from sqlalchemy.orm import Query
from typing import Optional

class BookRepository:
	def __init__(self, db: SessionLocal) -> None:
			self.db : SessionLocal= db



	def query_all(self) -> Query[Book]:
		return self.db.query(Book)



	def query_by_isbn(self, isbn: str) -> Query[Book]:
		return self.db.query(Book).filter(Book.isbn == isbn)



	def query_by_borrowed_status(self, is_borrowed: bool) -> Query[Book]:
		return self.db.query(Book).filter(Book.is_borrowed == is_borrowed)



	def query_by_keyword(self, keyword: str) -> Query[Book]:
		return self.db.query(Book).filter(
			or_(
				Book.title.ilike(f'%{keyword}%'),
				Book.author.ilike(f'%{keyword}%'),
				Book.isbn.ilike(f'%{keyword}%')
			))

	def query_available_books(self, keyword: Optional[str]=None) -> Query[Book]:
		query = self.db.query(Book).filter(Book.is_borrowed == False)
		if keyword:
			query = query.filter(
							or_(
								Book.title.ilike(f'%{keyword}%'),
								Book.author.ilike(f'%{keyword}%'),
								Book.isbn.ilike(f'%{keyword}%')
							))
		return query

	def add(self, book: Book) -> Book:
		self.db.add(book)
		return book



	def remove(self, book: Book) -> bool:
		self.db.delete(book)
		return True
