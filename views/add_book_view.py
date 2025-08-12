from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui.add_book import Ui_AddBook

class AddBookView(QMainWindow):
    def __init__(self, library):
        super().__init__()
        self.ui = Ui_AddBook()
        self.ui.setupUi(self)
        self.library = library
        self.ui.btn_add_book.clicked.connect(self.add_book)
        
    def add_book(self):
        title = self.ui.line_title.text()
        author = self.ui.line_author.text()
        isbn = self.ui.line_isbn.text()
        
        if not title or not author or not isbn:
            QMessageBox.warning(self, 'Error',  'please fill in all the fields')
            return
        success, msg = self.library.add_book(title, author, isbn)
        if success:
            QMessageBox.information(self, 'Done', msg)
        else:
            QMessageBox.warning(self, 'warning', msg)
