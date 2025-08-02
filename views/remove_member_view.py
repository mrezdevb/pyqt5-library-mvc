from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui.remove_member import Ui_RemoveMember

class RemoveMemberView(QMainWindow):
    def __init__(self, library):
        super().__init__()
        self.ui = Ui_RemoveMember()
        self.ui.setupUi(self)
        self.library = library
        self.ui.btn_remove_member.clicked.connect(self.remove_member)
        
    def remove_member(self):
        member_id = self.ui.line_member_id.text()
        
        if not member_id:
            QMessageBox.warning(self, 'Error',  'please fill in all the fields')
            return
        success, msg = self.library.remove_member(member_id)
        if success:
            QMessageBox.information(self, 'Done', msg)
        else:
            QMessageBox.warning(self, 'warning', msg)
