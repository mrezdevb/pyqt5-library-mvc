from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from ui.show_members import Ui_ShowMembers

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

    def load_members(self):
        members = self.library.show_members()
        if members is None:
            members = []

        self.ui.table_members.setRowCount(len(members))

        for row, member in enumerate(members):
            self.ui.table_members.setItem(row, 0, create_readonly_item(member.name))
            self.ui.table_members.setItem(row, 1, create_readonly_item(member.member_id))

