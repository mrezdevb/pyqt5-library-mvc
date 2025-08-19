from PyQt5.QtWidgets import QMainWindow, QMessageBox
from app.ui.remove_book import Ui_RemoveBook
from app.controllers.library_controller import LibraryController

class RemoveBookView(QMainWindow):

	def __init__(self, controller):
		super().__init__()
		self.ui = Ui_RemoveBook()
		self.ui.setupUi(self)
		self.controller = controller
		self.ui.btn_remove_book.clicked.connect(self.remove_book)





	def remove_book(self):
		isbn = self.ui.line_isbn.text().strip()


		if not isbn:
			QMessageBox.warning(self, 'Error', 'please fill in all the fields')
			return
		

		reply = QMessageBox.question(
			self,
			'Confirm Delete',
			f'Are you sure you want to remove this book "{isbn}"?',
			QMessageBox.Yes | QMessageBox.No
		)


		if reply != QMessageBox.Yes:
			return
		

		success, msg = self.controller.remove_book(isbn)


		if success:
			QMessageBox.information(self, 'Done', msg)
			self.ui.line_isbn.clear()
			self.ui.line_isbn.setFocus()

			
		else:
			QMessageBox.warning(self, 'warning', msg)


