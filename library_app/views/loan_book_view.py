from PyQt5.QtWidgets import QMainWindow, QMessageBox
from library_app.ui.loan_book import Ui_LoanBook
from library_app.controllers.library_controller import LibraryController


class LoanBookView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.ui = Ui_LoanBook()
        self.ui.setupUi(self)
        self.controller = controller
        self.ui.btn_loan_book.clicked.connect(self.loan_book)
        



    def loan_book(self):
        isbn = self.ui.line_isbn.text().strip()
        member_id = self.ui.line_member_id.text().strip()
        if not isbn or not member_id:
            QMessageBox.warning(self, 'Error',  'please fill in all the fields')
            return
        success, msg = self.controller.loan_book(member_id, isbn)
        if success:
            QMessageBox.information(self, 'Done', msg)
            self.ui.line_isbn.clear()
            self.ui.line_member_id.clear()
            self.ui.line_isbn.setFocus()
        else:
            QMessageBox.warning(self, 'warning', msg)




