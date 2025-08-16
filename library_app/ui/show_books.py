# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ShowBooks(object):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(800, 600)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 📌 لایه اصلی
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 40, 671, 400))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")

        # 📌 بخش جستجو و فیلتر
        self.search_layout = QtWidgets.QHBoxLayout()
        self.search_layout.setSpacing(10)
        
        self.search_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.search_input.setPlaceholderText("Search by title or author...")
        self.search_input.setFixedHeight(30)
        
        # 📌 فیلتر کتاب‌ها
        self.filter_combo = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.filter_combo.addItems(["All Books", "Available Books"])
        self.filter_combo.setFixedHeight(30)
        
        self.search_btn = QtWidgets.QPushButton("Search", self.verticalLayoutWidget)
        self.search_btn.setFixedHeight(30)

        # 📌 اضافه کردن به لایه جستجو
        self.search_layout.addWidget(self.search_input)
        self.search_layout.addWidget(self.filter_combo)
        self.search_layout.addWidget(self.search_btn)
        self.verticalLayout.addLayout(self.search_layout)

        # 📌 جدول کتاب‌ها
        self.table_books = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.table_books.setObjectName("table_books")
        self.table_books.setColumnCount(3)
        self.table_books.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table_books.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_books.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_books.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_books.setHorizontalHeaderItem(2, item)
        self.table_books.horizontalHeader().setDefaultSectionSize(130)
        self.table_books.horizontalHeader().setHighlightSections(True)
        self.table_books.horizontalHeader().setMinimumSectionSize(23)
        self.table_books.horizontalHeader().setSortIndicatorShown(False)
        self.table_books.horizontalHeader().setStretchLastSection(True)
        self.table_books.verticalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.table_books)

        # 📌 فضای پایینی (رزرو برای آینده)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show Books"))
        item = self.table_books.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.table_books.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.table_books.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Author"))
        item = self.table_books.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ISBN"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ShowBooks()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
