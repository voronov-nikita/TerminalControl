from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton
from PyQt5.QtGui import QIcon
import json
import sys
import os



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
        
        
class Zone3(MainLogic):
    def __init__(self) -> None:
        self.windowName:str = "Computer`s zone 3"
        
        self.initUI()
        
    def initUI(self):
        pass
    
    
class Zone5(MainLogic):
    def __init__(self) -> None:
        self.windowName:str = "Computer`s zone 5"
        
        self.initUI()
        
    def initUI(self):
        pass
        
        
def parsejson(file:str) -> dict:
    f = open(file, 'r')
    ls = ''.join(f.readlines())
    return json.loads(ls)


if __name__=="__main__":
    # ex = NetworkActions()
    # d = parsejson("mac.json")
    # ex.filltable(d)
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()