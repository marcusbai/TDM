from PyQt5.QtWidgets import QApplication, QMainWindow
from MainApp import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.pushButton_cha.clicked.connect(self.pushButton_cha_clicked)


    #def pushButton_cha_clicked(self):
        #self.set_title="111"

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainw = MainWindow()
    mainw.show()
    sys.exit(app.exec_())