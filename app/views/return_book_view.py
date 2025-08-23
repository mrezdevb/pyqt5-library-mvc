from PyQt5.QtWidgets import QMainWindow, QMessageBox
from app.ui.return_book import Ui_ReturnBook
from app.controllers.library_controller import LibraryController


class ReturnBookView(QMainWindow):

    def __init__(self, controller: LibraryController) -> None:
        super().__init__()
        self.ui: Ui_ReturnBook = Ui_ReturnBook()
        self.ui.setupUi(self)
        self.controller: LibraryController = controller
        self.ui.btn_return_book.clicked.connect(self.return_book)




    def return_book(self) -> None:
        isbn: str = self.ui.line_isbn.text().strip()
        member_id: str = self.ui.line_member_id.text().strip()


        if not isbn or not member_id:
            QMessageBox.warning(self, 'Error',  'please fill in all the fields')
            return
        
        success: bool
        msg: str
        success, msg = self.controller.return_book(member_id, isbn)


        if success:
            QMessageBox.information(self, 'Done', msg)
            self.ui.line_isbn.clear()
            self.ui.line_member_id.clear()
            self.ui.line_isbn.setFocus()

            
        else:
            QMessageBox.warning(self, 'warning', msg)
    
    
    
