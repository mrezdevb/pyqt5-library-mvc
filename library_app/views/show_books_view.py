from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from library_app.ui.show_books import Ui_ShowBooks


from PyQt5.QtCore import Qt

def create_readonly_item(text):
    item = QTableWidgetItem(text)
    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    return item




class ShowBooksView(QMainWindow):
    def __init__(self, library, main_view=None):
        super(ShowBooksView, self).__init__()
        self.ui = Ui_ShowBooks()
        self.ui.setupUi(self)
        self.library = library
        self.main_view = main_view
        self.load_books()
        self.ui.search_btn.clicked.connect(self.search_books)
    def load_books(self):
        books = self.library.show_books()
        if books is None:
            books = []

        self.ui.table_books.setRowCount(len(books))

        for row, book in enumerate(books):
            self.ui.table_books.setItem(row, 0, create_readonly_item(book.title))
            self.ui.table_books.setItem(row, 1, create_readonly_item(book.author))
            self.ui.table_books.setItem(row, 2, create_readonly_item(book.isbn))

    def search_books(self):
        keyword = self.ui.search_input.text().strip()

        books = self.library.search_books(keyword)
        if not books:
            QMessageBox.information(self, 'No Results', f'No books found for "{keyword}".')
            self.ui.table_books.setRowCount(0)
            return

        self.ui.table_books.setRowCount(len(books))
        for row, book in enumerate(books):
            self.ui.table_books.setItem(row, 0, create_readonly_item(book.title))
            self.ui.table_books.setItem(row, 1, create_readonly_item(book.author))
            self.ui.table_books.setItem(row, 2, create_readonly_item(book.isbn))
