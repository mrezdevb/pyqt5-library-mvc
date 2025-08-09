import sys 
from PyQt5.QtWidgets import QApplication
from library_app.views.main_window import MainView

def main():
	app = QApplication(sys.argv)
	window = MainView()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	
	main()
