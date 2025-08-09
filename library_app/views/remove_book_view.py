from PyQt5.QtWidgets import QMainWindow, QMessageBox
from library_app.ui.remove_book import Ui_RemoveBook


class RemoveBookView(QMainWindow):
	def __init__(self, library):
		super().__init__()
		self.ui = Ui_RemoveBook()
		self.ui.setupUi(self)
		self.library = library
		self.ui.btn_remove_book.clicked.connect(self.remove_book)
	def remove_book(self):
		isbn = self.ui.line_isbn.text()
		if not isbn:
			QMessageBox.warning(self, 'Error', 'please fill in all the fields')
			return
		success, msg = self.library.remove_book(isbn)
		if success:
			QMessageBox.information(self, 'Done', msg)
		else:
			QMessageBox.warning(self, 'warning', msg)

