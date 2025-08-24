from typing import List, Optional

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from app.controllers.library_controller import LibraryController
from app.models.book import Book
from app.ui.show_books import Ui_ShowBooks
from collections.abc import Sequence


def create_readonly_item(text: str) -> QTableWidgetItem:
    item: QTableWidgetItem = QTableWidgetItem(text)
    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # type: ignore[attr-defined]
    return item


class ShowBooksView(QMainWindow):

    def __init__(
        self, controller: LibraryController, main_view: Optional[QMainWindow] = None
    ) -> None:
        super(ShowBooksView, self).__init__()
        self.ui: Ui_ShowBooks = Ui_ShowBooks()
        self.ui.setupUi(self)
        self.controller: LibraryController = controller
        self.main_view: Optional[QMainWindow] = main_view
        self._setup_table_headers()
        self.last_search_keyword: str = ""
        self.last_filter_option: str = "All Books"
        self.load_books()
        controller.books_updated.connect(self.load_books)
        self.ui.search_btn.clicked.connect(self.search_books)

    def _setup_table_headers(self) -> None:
        self.ui.table_books.setColumnCount(4)
        self.ui.table_books.setHorizontalHeaderLabels(
            ["Title", "Author", "ISBN", "Status"]
        )

    def populate_table(self, books: Sequence[Book]) -> None:
        self.ui.table_books.setRowCount(len(books))

        for row, book in enumerate(books):
            self.ui.table_books.setItem(row, 0, create_readonly_item(book.title))
            self.ui.table_books.setItem(row, 1, create_readonly_item(book.author))
            self.ui.table_books.setItem(row, 2, create_readonly_item(book.isbn))
            status_text: str = "Borrowed" if book.is_borrowed else "Available"
            self.ui.table_books.setItem(row, 3, create_readonly_item(status_text))

    def load_books(self) -> None:

        if self.last_search_keyword:
            books: List[Book]
            status: str
            books, status = self.controller.search_books(
                self.last_search_keyword, self.last_filter_option
            )

            if status == "not found":
                self.ui.table_books.setRowCount(0)
                return
            self.populate_table(books)

        else:
            self.last_filter_option = self.ui.filter_combo.currentText()
            books = self.controller.show_books(self.last_filter_option) or []
            self.populate_table(books)

    def search_books(self) -> None:

        keyword: str = self.ui.search_input.text().strip()

        self.last_search_keyword = keyword if keyword else ""

        self.last_filter_option = self.ui.filter_combo.currentText()

        if not keyword:
            self.load_books()
            return

        filter_option: str = self.last_filter_option
        books: List[Book]
        status: str
        books, status = self.controller.search_books(keyword, filter_option)

        if status == "not found":
            QMessageBox.information(
                self, "No Results", f'No books found for "{keyword}".'
            )
            self.ui.table_books.setRowCount(0)
            return

        if status == "borrowed":
            QMessageBox.information(
                self, "Borrowed", f'Books matching "{keyword}" are currently borrowed.'
            )
            self.ui.table_books.setRowCount(0)
            return

        self.populate_table(books)
