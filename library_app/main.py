import sys

def main():
    from PyQt5.QtWidgets import QApplication
    from library_app.views.main_window import MainView
    from library_app.controllers.library_controller import LibraryController
    from library_app.db import SessionLocal

    app = QApplication(sys.argv)
    controller = LibraryController(SessionLocal())
    window = MainView(controller)
    window.show()
    try:
        app.exec_()
    finally:
        controller.close()

if __name__ == '__main__':
    main()