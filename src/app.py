# 
# 
# 
# 
# 


from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.name:str = "Termial Control"
        self.icon:str = ""
        
        self.initHeader()
        self.initUI()
    
    def initHeader(self) -> None:
        '''
        
        '''
        
        self.setWindowTitle(self.name)
        self.setWindowIcon(self.icon)
        self.showMaximized() 
    
    def initUI(self) -> None:
        '''
        
        '''
        pass
    

# start application if request from file
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())