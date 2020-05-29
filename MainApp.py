from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

import sys
class MainApp:

    def __init__(self):
        
        self.ui = loadUi('MainApp.ui')

        #self.ui.button.clicked.connect(self.handleCalc)

    #def handleCalc(self):

app = QApplication([])
MainApp = MainApp()
MainApp.ui.show()
app.exec_()