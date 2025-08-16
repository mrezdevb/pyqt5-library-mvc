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
        filter_option = self.ui.filter_combo.currentText()
        books= self.library.show_books(filter_option)
        if books is None:
            books = []

        self.ui.table_books.setRowCount(len(books))

        for row, book in enumerate(books):
            self.ui.table_books.setItem(row, 0, create_readonly_item(book.title))
            self.ui.table_books.setItem(row, 1, create_readonly_item(book.author))
            self.ui.table_books.setItem(row, 2, create_readonly_item(book.isbn))

    def search_books(self):
        keyword = self.ui.search_input.text().strip()
        filter_option = self.ui.filter_combo.currentText()

        books, status = self.library.search_books(keyword, filter_option)
        if status ==  'not found':
            QMessageBox.information(self, 'No Results', f'No books found for "{keyword}".')
            self.ui.table_books.setRowCount(0)
            return
        if status == 'borrowed':
            QMessageBox.information(self, 'Borrowed', f'Books matching "{keyword}" are currently borrowed.')
            self.ui.table_books.setRowCount(0)

        self.ui.table_books.setRowCount(len(books))
        for row, book in enumerate(books):
            self.ui.table_books.setItem(row, 0, create_readonly_item(book.title))
            self.ui.table_books.setItem(row, 1, create_readonly_item(book.author))
            self.ui.table_books.setItem(row, 2, create_readonly_item(book.isbn))
