import sys


def main() -> None:
    from PyQt5.QtWidgets import QApplication

    from app.controllers.library_controller import LibraryController
    from app.db.db import SessionLocal
    from app.db.unit_of_work import UnitOfWork
    from app.views.main_window import MainView

    uow: UnitOfWork = UnitOfWork(SessionLocal)
    controller: LibraryController = LibraryController(uow)
    app: QApplication = QApplication(sys.argv)

    window: MainView = MainView(controller)
    window.show()

    try:
        app.exec_()

    finally:
        controller.close()


if __name__ == "__main__":
    main()
