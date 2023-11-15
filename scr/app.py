from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton
from PyQt5.QtGui import QIcon
import sys


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.windowName = "Terminal Control"
        self.windowSize = (400, 500)
        self.windowIcon = ""
        
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.windowName)
        self.setFixedSize(self.width(), self.height())
        
        
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()