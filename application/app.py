import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon
import json
import sys
import os


JSONFILE:str = "../hosts.json"


class MainLogic(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        
    def openTerminal(self, user:str, host=None, numberZone=None, numberComp=None) -> None:
        '''
        
        '''
        if host is not None:
            os.system(f"cmd /c start cmd /k ssh {user}@{host}")
            self.close()
            return 
        os.system(f"cmd /c start cmd /k ssh {user}@{parsejson(JSONFILE)[numberZone][numberComp]}.local")
        self.close()


class Zone3(MainLogic):
    def __init__(self, activeUser:str="root") -> None:
        super().__init__()
        self.windowName:str = "Zone 3"
        self.windowSize = (400, 400)
        
        self.user = activeUser
        
        self.initUI()
        
    def initUI(self):
        self.setFixedSize(*self.windowSize)
        self.setWindowTitle(self.windowName)
        
        
        grid = QGridLayout()
        count = 3
        for number in range(12):
            button = QPushButton(self)
            button.setText(str(number+1))
            button.setFixedSize(50, 50)
            button.clicked.connect(lambda: self.openTerminal(
                                                            user=self.user,
                                                            numberZone="Zone3", 
                                                            numberComp=str(number+1)
                                                            )
                                    )
            button.setStyleSheet(
                """
                background-color: #116530;
                color: #f28500;
                """
            )
            if number >= 8:
                button.setText(str(count+number+1))
                count -= 2
                grid.addWidget(button, number - 8, 0)
            else:
                grid.addWidget(button, number, 1)
        self.setLayout(grid)


class Zone5(MainLogic):
    def __init__(self, activeUser:str="root") -> None:
        super().__init__()
        self.windowName:str = "Zone 5"
        
        self.user = activeUser
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.windowName)
        
        
        grid = QGridLayout()
        count = 3
        for number in range(30):
            button = QPushButton(self)
            button.setText(str(number+1))
            button.setFixedSize(50, 50)
            button.clicked.connect(lambda: self.openTerminal(
                                                            user=self.user,
                                                            numberZone="Zone5", 
                                                            numberComp=str(number+1)
                                                            )
                                    )
            button.setStyleSheet(
                """
                background-color: #116530;
                color: #f28500;
                """
            )
            if number <= 8:
                button.setText(str(count+number+1))
                grid.addWidget(button, number - 8, 0)
            else:
                grid.addWidget(button, number, 1)
        self.setLayout(grid)


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.windowName = "Terminal Control"
        self.windowSize = (600, 800)
        self.windowIcons = ""
        
        self.buttonSize = (200, 200)
        
        self.initUI()
        
    def initUI(self) -> None:
        
        self.setWindowTitle(self.windowName)
        self.setFixedSize(self.width(), self.height())
        
        self.ex = None
        
        button3 = QPushButton(self)
        button3.resize(*self.buttonSize)
        button3.setText("Zone3")
        button3.move((self.windowSize[0] + self.buttonSize[0])//10, (self.windowSize[1]+self.buttonSize[1])//10)
        button3.clicked.connect(self.openZone3)
        
        button5 = QPushButton(self)
        button5.resize(*self.buttonSize)
        button5.setText("Zone5")
        button5.move((self.windowSize[0] + self.buttonSize[0])//2, (self.windowSize[1]+self.buttonSize[1])//10)
        button5.clicked.connect(self.openZone5)
        
        self.text = QLineEdit(self)
        self.text.resize(200, 40)
        self.text.move((self.windowSize[0]-200)//2, self.windowSize[1]//2)
        self.text.setPlaceholderText("User(root)")
    
    def openZone3(self):
        self.ex = Zone3(activeUser=self.text.text)
        self.ex.show()
        
    def openZone5(self):
        self.ex = Zone5(activeUser=self.text.text)
        self.ex.show()
    


def parsejson(file:str) -> dict:
    f = open(file, 'r')
    ls = ''.join(f.readlines())
    return json.loads(ls)


if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())