# 
# 
# 
# 
# 


from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout,\
    QSizePolicy, QPushButton
from PyQt5.QtGui import QIcon

from logic import SpecialAction, parseData
from threading import Thread
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()
        
        self.name:str = "Termial Control"
        self.icon:str = "../assets/mainIcon.jpg"
        
        self.sizeWindow = (300, 500)
        
        self.initHeader()
        self.initUI()
        
        self.show()
    
    def initHeader(self) -> None:
        '''
        
        '''
        
        self.setGeometry(600, 500, *self.sizeWindow)
        self.setWindowTitle(self.name)
        self.setWindowIcon(QIcon(self.icon))
        # self.showMaximized() 
    
    def initUI(self) -> None:
        '''
        
        '''
        
        layout = QVBoxLayout(self)
        buttons = parseData("data.json")["Zones"]
        
        self.ls = dict()
        
        for i in range(len(buttons)):
            
            title = list(buttons.keys())[i]
            size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            
            button = QPushButton(str(title), self)
            button.setSizePolicy(size_policy)
            button.clicked.connect(lambda: self.newWindow())
            
            layout.addWidget(button)

        self.setLayout(layout)
        
        
    def newWindow(self) -> None:
        '''
        
        '''
        pass
    

# start application if request from file
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())