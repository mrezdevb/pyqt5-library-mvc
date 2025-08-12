from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui.add_member import Ui_AddMember

class AddMemberView(QMainWindow):
    def __init__(self, library):
        super().__init__()
        self.ui = Ui_AddMember()
        self.ui.setupUi(self)
        self.library = library
        self.ui.btn_add_member.clicked.connect(self.add_member)
        
    def add_member(self):
        name = self.ui.line_name.text()
        member_id = self.ui.line_member_id.text()
        
        if not name or not member_id:
            QMessageBox.warning(self, 'Error',  'please fill in all the fields')
            return
        success, msg = self.library.add_member(name, member_id)
        if success:
            QMessageBox.information(self, 'Done', msg)
        else:
            QMessageBox.warning(self, 'warning', msg)
