from PyQt5.QtWidgets import QMainWindow, QMessageBox
from app.ui.remove_member import Ui_RemoveMember
from app.controllers.library_controller import LibraryController


class RemoveMemberView(QMainWindow):

    def __init__(self, controller: LibraryController) -> None:
        super().__init__()
        self.ui: Ui_RemoveMember = Ui_RemoveMember()
        self.ui.setupUi(self)
        self.controller: LibraryController = controller
        self.ui.btn_remove_member.clicked.connect(self.remove_member)
        


    def remove_member(self) -> None:
        member_id: str = self.ui.line_member_id.text().strip()
        

        if not member_id:
            QMessageBox.warning(self, 'Error',  'please fill in all the fields')
            return
        

        reply: QMessageBox.StandardButton = QMessageBox.question(
            self,
            'Confirm Delete',
            f'Are you sure you want to remove member "{member_id}" ?',
            QMessageBox.Yes | QMessageBox.No
        )


        if reply != QMessageBox.Yes:
            return
        success: bool
        msg: str

        success, msg = self.controller.remove_member(member_id)


        if success:
            QMessageBox.information(self, 'Done', msg)
            self.ui.line_member_id.clear()
            self.ui.line_member_id.setFocus()

            
        else:
            QMessageBox.warning(self, 'warning', msg)



   