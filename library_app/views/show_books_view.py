from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from library_app.ui.show_books import Ui_ShowBooks
from PyQt5.QtCore import Qt
from library_app.controllers.library_controller import LibraryController


def create_readonly_item(text):
    item = QTableWidgetItem(text)
    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    return item


class ShowBooksView(QMainWindow):
    def __init__(self, controller, main_view=None):
        super(ShowBooksView, self).__init__()
        self.ui = Ui_ShowBooks()
        self.ui.setupUi(self)
        self.controller = controller
        self.main_view = main_view
        self._setup_table_headers()
        self.last_search_keyword = ''
        self.last_filter_option = 'All Books'
        self.load_books()
        controller.books_updated.connect(self.load_books)
        self.ui.search_btn.clicked.connect(self.search_books)


    def _setup_table_headers(self):
        self.ui.table_books.setColumnCount(4)
        self.ui.table_books.setHorizontalHeaderLabels(['Title', 'Author', 'ISBN', 'Status'])


    def populate_table(self, books):
        self.ui.table_books.setRowCount(len(books))
        for row, book in enumerate(books):
            self.ui.table_books.setItem(row, 0, create_readonly_item(book.title))
            self.ui.table_books.setItem(row, 1, create_readonly_item(book.author))
            self.ui.table_books.setItem(row, 2, create_readonly_item(book.isbn))
            status_text = 'Borrowed' if book.is_borrowed else 'Available'
            self.ui.table_books.setItem(row, 3, create_readonly_item(status_text))


    def load_books(self):
        if self.last_search_keyword:
            books, status = self.controller.search_books(self.last_search_keyword, self.last_filter_option)
            if status == 'not found':
                self.ui.table_books.setRowCount(0)
                return
            self.populate_table(books)
        else:
            self.last_filter_option = self.ui.filter_combo.currentText()
            books= self.controller.show_books(self.last_filter_option) or []
            self.populate_table(books)


    def search_books(self):
        keyword = self.ui.search_input.text().strip()
        self.last_search_keyword = keyword if keyword else ''
        self.last_filter_option = self.ui.filter_combo.currentText()
        if not keyword:
            self.load_books()
            return
        filter_option = self.last_filter_option
        books, status = self.controller.search_books(keyword, filter_option)
        if status ==  'not found':
            QMessageBox.information(self, 'No Results', f'No books found for "{keyword}".')
            self.ui.table_books.setRowCount(0)
            return
        if status == 'borrowed':
            QMessageBox.information(self, 'Borrowed', f'Books matching "{keyword}" are currently borrowed.')
            self.ui.table_books.setRowCount(0)
            return
        self.populate_table(books)




    
