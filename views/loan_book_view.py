from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui.loan_book import Ui_LoanBook

class LoanBookView(QMainWindow):
    def __init__(self, library):
        super().__init__()
        self.ui = Ui_LoanBook()
        self.ui.setupUi(self)
        self.library = library
        self.ui.btn_loan_book.clicked.connect(self.loan_book)
    def loan_book(self):
        isbn = self.ui.line_isbn.text()
        member_id = self.ui.line_member_id.text()
        if not isbn or not member_id:
            QMessageBox.warning(self, 'Error',  'please fill in all the fields')
            return
        success, msg = self.library.loan_book(member_id, isbn)
        if success:
            QMessageBox.information(self, 'Done', msg)
        else:
            QMessageBox.warning(self, 'warning', msg)