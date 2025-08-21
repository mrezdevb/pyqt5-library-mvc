import sys




def main():
    from PyQt5.QtWidgets import QApplication
    from app.views.main_window import MainView
    from app.db.db import SessionLocal
    from app.controllers.library_controller import LibraryController
    from app.db.unit_of_work import UnitOfWork



    app = QApplication(sys.argv)
    uow = UnitOfWork(SessionLocal)
    controller = LibraryController(uow)
    window = MainView(controller)
    window.show()


    try:
        app.exec_()

    finally:
        controller.close()



if __name__ == '__main__':
    main()