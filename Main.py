from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import *
from MainApp import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./data/tdm.db')
        db.open()
        model1=QSqlTableModel(None,db)
        model1.setTable('tdm')
        model1.select()
        self.ui.tableView.setModel(model1)
        self.ui.tableView.show()
        #self.ui.pushButton_cha.clicked.connect(self.pushButton_cha_clicked)
    #def pushButton_cha_clicked(self):
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainw = MainWindow()
    mainw.show()
    sys.exit(app.exec_())