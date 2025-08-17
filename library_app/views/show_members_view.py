from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from library_app.ui.show_members import Ui_ShowMembers

from PyQt5.QtCore import Qt

def create_readonly_item(text):
    item = QTableWidgetItem(text)
    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    return item




class ShowMembersView(QMainWindow):
    def __init__(self, library, main_view=None):
        super(ShowMembersView, self).__init__()
        self.ui = Ui_ShowMembers()
        self.ui.setupUi(self)
        self.library = library
        self.main_view = main_view
        self.load_members()
        self.ui.search_btn.clicked.connect(self.search_members)
    def load_members(self):
        members = self.library.show_members()
        if members is None:
            members = []
        self.ui.table_members.setColumnCount(3)
        self.ui.table_members.setHorizontalHeaderLabels(['Name', 'Member ID', 'Borrowed Books'])
        self.ui.table_members.setRowCount(len(members))

        for row, member in enumerate(members):
            self.ui.table_members.setItem(row, 0, create_readonly_item(member['name']))
            self.ui.table_members.setItem(row, 1, create_readonly_item(member['member_id']))
            self.ui.table_members.setItem(row, 2, create_readonly_item(member['borrowed_books'] or '-'))
    
    
    
    def search_members(self):
        keyword = self.ui.search_input.text().strip()
        # if not keyword:
        #     QMessageBox.warning(self, 'Warning', 'Please enter a keyword for search.')
        #     return

        members = self.library.search_members(keyword)
        if not members:
            QMessageBox.information(self, 'No Result', f'No Members found for "{keyword}".')
            self.ui.table_members.setRowCount(0)
            return 

        self.ui.table_members.setColumnCount(3)
        self.ui.table_members.setHorizontalHeaderLabels(['Name', 'Member ID', 'Borrowed Books'])
        self.ui.table_members.setRowCount(len(members))

        for row, member in enumerate(members):
            self.ui.table_members.setItem(row, 0, create_readonly_item(member['name']))
            self.ui.table_members.setItem(row, 1, create_readonly_item(member['member_id']))
            self.ui.table_members.setItem(row, 2, create_readonly_item(member['borrowed_books'] or '-'))
