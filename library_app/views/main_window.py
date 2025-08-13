from PyQt5 import QtWidgets
from library_app.ui.main import Ui_MainWindow
from library_app.controllers.library import LibraryManagement
from library_app.views.add_book_view import AddBookView
from library_app.views.remove_book_view import RemoveBookView
from library_app.views.add_member_view import AddMemberView
from library_app.views.remove_member_view import RemoveMemberView
from library_app.views.show_books_view import ShowBooksView
from library_app.views.show_members_view import ShowMembersView
from library_app.views.loan_book_view import LoanBookView
from library_app.views.return_book_view import ReturnBookView
from library_app.db import SessionLocal

class MainView(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.db_session = SessionLocal()
		self.library = LibraryManagement(self.db_session)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.btn_add_book.clicked.connect(self.open_add_book)
		self.ui.btn_remove_book.clicked.connect(self.open_remove_book)
		self.ui.btn_add_member.clicked.connect(self.open_add_member)
		self.ui.btn_remove_member.clicked.connect(self.open_remove_member)
		self.ui.btn_show_books.clicked.connect(self.open_show_books)
		self.ui.btn_show_members.clicked.connect(self.open_show_members)
		self.ui.btn_loan_book.clicked.connect(self.open_loan_book)
		self.ui.btn_return_book.clicked.connect(self.open_return_book)
	def open_add_book(self):
		self.add_book_dialog = AddBookView(self.library)
		self.add_book_dialog.show()
	
	def open_remove_book(self):
		self.remove_book_dialog = RemoveBookView(self.library)
		self.remove_book_dialog.show()
	
	def open_add_member(self):
		self.add_member_dialog = AddMemberView(self.library)
		self.add_member_dialog.show()

	def open_remove_member(self):
		self.remove_member_dialog = RemoveMemberView(self.library)
		self.remove_member_dialog.show()
	
	def open_show_books(self):
		self.show_books_dialog = ShowBooksView(self.library)
		self.show_books_dialog.show()

	def open_show_members(self):
		self.show_members_dialog = ShowMembersView(self.library)
		self.show_members_dialog.show()
	def open_loan_book(self):
		self.loan_book_dialog = LoanBookView(self.library)
		self.loan_book_dialog.show()
	def open_return_book(self):
		self.return_book_dialog = ReturnBookView(self.library)
		self.return_book_dialog.show()
