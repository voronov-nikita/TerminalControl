from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton
from PyQt5.QtGui import QIcon
import subprocess
import socket
import json
import sys
import os


class NetworkActions():
    def __init__(self):
        self.networkip = socket.gethostbyname(socket.gethostname())
        print(self.networkip)
    
    def network_scan(self) -> str:
        '''
        Executes a command to fill in the arp table relative to the 
        ip address of the user who is making the request.
        '''
        os.system(rf"for /L %a in (1,1,254) do @start /b ping 192.168.{0}.%a -n 2 > nul")
        return subprocess.check_output(['arp', '-a'])
    
    def get_network(self) -> str:
        '''
        Returns the value of the user's current ip address. 
        
        It is used mainly when creating an 
        arp table and further assembling this bacillus into a dictionary.
        '''
        return self.networkip


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.actions = NetworkActions()
        
        self.windowName = "Terminal Control"
        self.windowSize = (400, 500)
        self.windowIcon = ""
        
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.windowName)
        self.setFixedSize(self.width(), self.height())
        
        self.box = QComboBox(self)
        self.box.addItems(["Zone 2", "Zone 3"])
        
        self.button = QPushButton(self)
        self.button.setText("Connect")
        self.button.clicked.connect(self.InfillArp)


    def InfillArp(self):
        print()
        
def parsejson(file:str) -> dict:
    return json.loads(file)


if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()