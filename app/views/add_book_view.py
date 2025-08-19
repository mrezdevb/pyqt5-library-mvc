from PyQt5.QtWidgets import QMainWindow, QMessageBox
from app.ui.add_book import Ui_AddBook
from app.controllers.library_controller import LibraryController


class AddBookView(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.ui = Ui_AddBook()
        self.ui.setupUi(self)
        self.controller = controller
        self.ui.btn_add_book.clicked.connect(self.add_book)
        




    def add_book(self):
        title = self.ui.line_title.text().strip()
        author = self.ui.line_author.text().strip()
        isbn = self.ui.line_isbn.text().strip()
        


        if not title or not author or not isbn:
            QMessageBox.warning(self, 'Error',  'please fill in all the fields')
            return
        

        success, msg = self.controller.add_book(title, author, isbn)


        if success:
            QMessageBox.information(self, 'Done', msg)
            self.ui.line_title.clear()
            self.ui.line_author.clear()
            self.ui.line_isbn.clear()
            self.ui.line_title.setFocus()

            
        else:
            QMessageBox.warning(self, 'warning', msg)

