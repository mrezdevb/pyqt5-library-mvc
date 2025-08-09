from PyQt5.QtWidgets import QMainWindow, QMessageBox
from library_app.ui.return_book import Ui_ReturnBook

class ReturnBookView(QMainWindow):
    def __init__(self, library):
        super().__init__()
        self.ui = Ui_ReturnBook()
        self.ui.setupUi(self)
        self.library = library
        self.ui.btn_return_book.clicked.connect(self.return_book)
    def return_book(self):
        isbn = self.ui.line_isbn.text()
        member_id = self.ui.line_member_id.text()
        if not isbn or not member_id:
            QMessageBox.warning(self, 'Error',  'please fill in all the fields')
            return
        success, msg = self.library.return_book(member_id, isbn)
        if success:
            QMessageBox.information(self, 'Done', msg)
        else:
            QMessageBox.warning(self, 'warning', msg)
