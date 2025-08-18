from library_app.services.book_service import BookService
from library_app.services.member_service import MemberService
from library_app.services.loan_service import LoanService
from library_app.db import SessionLocal
from PyQt5.QtCore import QObject, pyqtSignal

class LibraryController(QObject):
	books_updated = pyqtSignal()
	members_updated = pyqtSignal()
	def __init__(self, session=None):
		super().__init__()
		self.session = session or SessionLocal()
		self.book_service = BookService(self.session)
		self.member_service = MemberService(self.session)
		self.loan_service = LoanService(self.session)

	def _commit_ok(self, ok:bool):
		if ok:
			self.session.commit()
		else:
			self.session.rollback()
		return ok
	

	def add_book(self, title, author, isbn):
		ok, msg = self.book_service.add_book(title, author, isbn)
		if self._commit_ok(ok):
			self.books_updated.emit()
		return ok, msg
	

	def remove_book(self, isbn):
		ok, msg = self.book_service.remove_book(isbn)
		if self._commit_ok(ok):
			self.books_updated.emit()
			self.members_updated.emit()
		return ok, msg
	
	def add_member(self, name, member_id):
		ok, msg = self.member_service.add_member(name, member_id)
		if self._commit_ok(ok):
			self.members_updated.emit()
		return ok, msg
	
	def remove_member(self, member_id):
		ok, msg = self.member_service.remove_member(member_id)
		if self._commit_ok(ok):
			self.members_updated.emit()
			self.books_updated.emit()
		return ok, msg
	
	def loan_book(self, member_id, isbn):
		ok, msg =  self.loan_service.loan_book(member_id, isbn)
		if self._commit_ok(ok):
			self.books_updated.emit()
			self.members_updated.emit()
		return ok, msg
	

	def return_book(self, member_id, isbn):
		ok, msg = self.loan_service.return_book(member_id, isbn)
		if self._commit_ok(ok):
			self.books_updated.emit()
			self.members_updated.emit()
		return ok, msg
	

	def show_books(self, filter_option=None):
		return self.book_service.show_books(filter_option)
	

	def search_books(self, keyword, filter_option):
		return self.book_service.search_books(keyword, filter_option)
	
	def show_members(self, raw=False):
		return self.member_service.show_members(raw)
	

	def search_members(self, keyword, raw=False):
		return self.member_service.search_members(keyword, raw)
	
	def close(self):
		self.session.close()
