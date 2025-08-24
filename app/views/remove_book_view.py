from PyQt5.QtWidgets import QMainWindow, QMessageBox

from app.controllers.library_controller import LibraryController
from app.ui.remove_book import Ui_RemoveBook


class RemoveBookView(QMainWindow):

    def __init__(self, controller: LibraryController) -> None:
        super().__init__()
        self.ui: Ui_RemoveBook = Ui_RemoveBook()
        self.ui.setupUi(self)
        self.controller: LibraryController = controller
        self.ui.btn_remove_book.clicked.connect(self.remove_book)

    def remove_book(self) -> None:
        isbn: str = self.ui.line_isbn.text().strip()

        if not isbn:
            QMessageBox.warning(self, "Error", "please fill in all the fields")
            return

        reply: QMessageBox.StandardButton = QMessageBox.question(
            self,
            "Confirm Delete",
            f'Are you sure you want to remove this book "{isbn}"?',
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply != QMessageBox.Yes:
            return

        success: bool
        msg: str
        success, msg = self.controller.remove_book(isbn)

        if success:
            QMessageBox.information(self, "Done", msg)
            self.ui.line_isbn.clear()
            self.ui.line_isbn.setFocus()

        else:
            QMessageBox.warning(self, "warning", msg)
