from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from app.ui.show_members import Ui_ShowMembers
from PyQt5.QtCore import Qt
from app.controllers.library_controller import LibraryController


def create_readonly_item(text):
    item = QTableWidgetItem(text)
    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    return item






class ShowMembersView(QMainWindow):

    def __init__(self, controller, main_view=None):
        super(ShowMembersView, self).__init__()
        self.ui = Ui_ShowMembers()
        self.ui.setupUi(self)
        self.main_view = main_view
        self.controller = controller
        self._setup_table_headers()
        self.last_search_keyword = ''
        self.load_members()
        controller.members_updated.connect(self.load_members)
        self.ui.search_btn.clicked.connect(self.search_members)



    def _setup_table_headers(self):
        self.ui.table_members.setColumnCount(3)
        self.ui.table_members.setHorizontalHeaderLabels(['Name', 'Member ID', 'Borrowed Books'])




    def populate_table(self, members):
        self.ui.table_members.setRowCount(len(members))
        for row, member in enumerate(members):
            self.ui.table_members.setItem(row, 0, create_readonly_item(member.get('name', '-')))
            self.ui.table_members.setItem(row, 1, create_readonly_item(member.get('member_id', '-')))
            self.ui.table_members.setItem(row, 2, create_readonly_item(member.get('borrowed_books') or '-'))




    def load_members(self):
        if self.last_search_keyword:
            members = self.controller.search_members(self.last_search_keyword) or []
            self.populate_table(members)


        else:
            members = self.controller.show_members() or []
            self.populate_table(members)


    def search_members(self):
        keyword = self.ui.search_input.text().strip()

        self.last_search_keyword = keyword if keyword else ''

        if not keyword:
            self.load_members()
            return
        

        members = self.controller.search_members(keyword) or []

        if not members:
            QMessageBox.information(self, 'No Result', f'No Members found for "{keyword}".')
            self.ui.table_members.setRowCount(0)
            return
        
        
        self.populate_table(members)
