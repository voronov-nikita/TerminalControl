from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout
from PyQt5.QtCore import QRect
import sys



class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.windowSize = (900, 600)
        self.windowName = "Terminal Control"
        
        self.buttonSize = (200, 200)
        
        self.InitUI()
        
    def InitUI(self):
        self.setGeometry(QRect(self.width(), self.height()//2, *self.windowSize))
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle(self.windowName)
        
        
        


if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    app.exec_()
    