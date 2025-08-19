from PyQt5 import QtWidgets
from app.ui.main import Ui_MainWindow
from app.controllers.library_controller import LibraryController
from app.views.add_book_view import AddBookView
from app.views.remove_book_view import RemoveBookView
from app.views.add_member_view import AddMemberView
from app.views.remove_member_view import RemoveMemberView
from app.views.show_books_view import ShowBooksView
from app.views.show_members_view import ShowMembersView
from app.views.loan_book_view import LoanBookView
from app.views.return_book_view import ReturnBookView
from app.db.db import SessionLocal

class MainView(QtWidgets.QMainWindow):

	def __init__(self, controller: LibraryController):
		super().__init__()
		self.controller = controller
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)



		self.ui.btn_add_book.clicked.connect(lambda: self.open_window(AddBookView, 'add_book_dialog'))
		self.ui.btn_remove_book.clicked.connect(lambda: self.open_window(RemoveBookView, 'remove_book_dialog'))
		self.ui.btn_add_member.clicked.connect(lambda: self.open_window(AddMemberView, 'add_member_dialog'))
		self.ui.btn_remove_member.clicked.connect(lambda: self.open_window(RemoveMemberView, 'remove_member_dialog'))
		self.ui.btn_show_books.clicked.connect(lambda: self.open_window(ShowBooksView, 'show_books_dialog'))
		self.ui.btn_show_members.clicked.connect(lambda: self.open_window(ShowMembersView, 'show_members_dialog'))
		self.ui.btn_loan_book.clicked.connect(lambda: self.open_window(LoanBookView, 'loan_book_dialog'))
		self.ui.btn_return_book.clicked.connect(lambda: self.open_window(ReturnBookView, 'return_book_dialog'))
	
	


	def open_window(self, window_class, attr_name):
		if not hasattr(self, attr_name) or not getattr(self, attr_name).isVisible():
			setattr(self, attr_name, window_class(self.controller))


		window = getattr(self, attr_name)
		window.show()
		window.raise_()
		window.activateWindow()



	def closeEvent(self, event):
		for attr in dir(self):
			if attr.endswith("_dialog"):
				dialog = getattr(self, attr, None)
				if dialog and dialog.isVisible():
					dialog.close()

					
		self.controller.close()
		super().closeEvent(event)
