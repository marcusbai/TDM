from PyQt5.QtWidgets import QApplication, QMainWindow
from MainApp import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_4.clicked.connect(self.pushButton_4_clicked)


    def pushButton_4_clicked(self):
        print('aaaaaaa')

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainw = MainWindow()
    mainw.show()
    sys.exit(app.exec_())