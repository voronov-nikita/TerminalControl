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
        
        self.initHeader()
        self.initUI()
    
    def initHeader(self) -> None:
        '''
        
        '''
    
    def initUI(self) -> None:
        '''
        
        '''
        pass
    

# start application if request from file
if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())