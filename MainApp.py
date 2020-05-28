#from PySide2.QtWidgets import QApplication, QMessageBox
#from PySide2.QtUiTools import QUiLoader
from PyQt5 import QtWidgets, ui

import sys
class MainApp:

    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('MainApp.ui')

        #self.ui.button.clicked.connect(self.handleCalc)

    #def handleCalc(self):

app = QApplication([])
ma = MainApp()
ma.ui.show()
app.exec_()