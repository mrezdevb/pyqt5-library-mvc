# -*- coding: utf-8 -*-

from typing import Callable

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_ShowMembers(object):
    def setupUi(self, MainWindow: QMainWindow) -> None:
        MainWindow.setFixedSize(800, 600)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 40, 671, 400))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")

        self.search_layout = QtWidgets.QHBoxLayout()
        self.search_layout.setSpacing(10)
        self.search_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.search_input.setPlaceholderText("Search by name or member ID...")
        self.search_input.setFixedHeight(30)
        self.search_btn = QtWidgets.QPushButton("Search", self.verticalLayoutWidget)
        self.search_btn.setFixedHeight(30)
        self.search_layout.addWidget(self.search_input)
        self.search_layout.addWidget(self.search_btn)
        self.verticalLayout.addLayout(self.search_layout)

        self.table_members = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.table_members.setObjectName("table_members")
        self.table_members.setColumnCount(3)
        self.table_members.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_members.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()

        self.table_members.setHorizontalHeaderItem(2, item)

        h_header = self.table_members.horizontalHeader()
        if h_header is not None:
            h_header.setDefaultSectionSize(190)
            h_header.setHighlightSections(True)
            h_header.setMinimumSectionSize(23)
            h_header.setSortIndicatorShown(False)
            h_header.setStretchLastSection(True)

        v_header = self.table_members.verticalHeader()
        if v_header is not None:
            v_header.setVisible(True)

        self.verticalLayout.addWidget(self.table_members)

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 490, 101, 61))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: QMainWindow) -> None:
        _translate: Callable[[str, str], str] = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show Members"))

        v_item = self.table_members.verticalHeaderItem(0)
        if v_item is not None:
            v_item.setText(_translate("MainWindow", "1"))

        h_item = self.table_members.horizontalHeaderItem(0)
        if h_item is not None:
            h_item.setText(_translate("MainWindow", "Name"))

        h_item = self.table_members.horizontalHeaderItem(1)
        if h_item is not None:
            h_item.setText(_translate("MainWindow", "Member ID"))

        h_item = self.table_members.horizontalHeaderItem(2)
        if h_item is not None:
            h_item.setText(_translate("MainWindow", "Borrowed Books"))


if __name__ == "__main__":
    import sys

    app: QApplication = QtWidgets.QApplication(sys.argv)
    MainWindow: QMainWindow = QtWidgets.QMainWindow()
    ui: Ui_ShowMembers = Ui_ShowMembers()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
