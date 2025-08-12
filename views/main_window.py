from PyQt5 import QtWidgets
from ui.main import Ui_MainWindow
from controllers.library import LibraryManagement
from views.add_book_view import AddBookView
from views.remove_book_view import RemoveBookView
from views.add_member_view import AddMemberView
from views.remove_member_view import RemoveMemberView
from views.show_books_view import ShowBooksView
from views.show_members_view import ShowMembersView
from views.loan_book_view import LoanBookView
from views.return_book_view import ReturnBookView


class MainView(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.library = LibraryManagement()
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