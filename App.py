from PyQt5.QtWidgets import QApplication, QMainWindow
from Main import MainWindow
import sys

app= QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())