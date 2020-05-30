from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

import sys
class MainApp:

    def __init__(self):
        
        self.ui = loadUi('MainApp.ui')
        self.ui.pushButton_4.clicked.connect(self.handleCalc)

    def handleCalc(self):


app = QApplication(sys.argv)
MainApp = MainApp()
MainApp.ui.show()
sys.exit(app.exec_())