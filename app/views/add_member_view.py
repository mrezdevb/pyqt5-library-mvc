from PyQt5.QtWidgets import QMainWindow, QMessageBox
from app.ui.add_member import Ui_AddMember
from app.controllers.library_controller import LibraryController



class AddMemberView(QMainWindow):

    def __init__(self, controller: LibraryController) -> None:
        super().__init__()
        self.ui: Ui_AddMember = Ui_AddMember()
        self.ui.setupUi(self)
        self.controller: LibraryController = controller
        self.ui.btn_add_member.clicked.connect(self.add_member)
        




    def add_member(self) -> None:
        name: str = self.ui.line_name.text().strip()
        member_id: str = self.ui.line_member_id.text().strip()
        


        if not name or not member_id:
            QMessageBox.warning(self, 'Error',  'please fill in all the fields')
            return
        
        success: bool
        msg: str
        success, msg = self.controller.add_member(name, member_id)


        if success:
            QMessageBox.information(self, 'Done', msg)
            self.ui.line_name.clear()
            self.ui.line_member_id.clear()
            self.ui.line_name.setFocus()

            
        else:
            QMessageBox.warning(self, 'warning', msg)



