from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication,\
    QListWidget, QListWidgetItem, QScrollArea

import configparser
import json
import sys

sys.path.append("../")

# извлечение конфигов
config = configparser.ConfigParser()
config.read("config.ini")

LIST_ACTION: list = eval(config['App'].get('actions'))


class MoreAction(QWidget):
    def __init__(self, title:str="Unknown Host", mainWindow:QWidget="") -> None:
        '''
        
        '''
        
        super().__init__()

        self.title = title
        self.mainWindow = mainWindow

        self.initUI()

    def initUI(self) -> None:
        '''
        Инициализация основного интерфейса приложения.
        '''

        layout = QVBoxLayout()
        
        label = QLabel(self.title)
        layout.addWidget(label)

        self.lsWidget = QListWidget()
        
        # добавляем все кнопки из массива хостов
        for elem in LIST_ACTION:
            button = QPushButton(elem)
            action = elem
            button.clicked.connect(lambda state, self=self, act=action: eval(f"self.{act.replace(" ", "")}()"))
            
            item = QListWidgetItem()
            
            self.lsWidget.addItem(item)
            self.lsWidget.setItemWidget(item, button)
        
        
        layout.addWidget(self.lsWidget)
        self.setLayout(layout)
    
    # Действия описаны здесь
    def connect(self):
        print("Connect")
        
    def wakeonlan(self):
        print("WakeOnLan")
        
    def poweroff(self):
        print("Poweroff")
        
    def openbrowser(self):
        print("OpenBrowser")


if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MoreAction()
    ex.show()
    sys.exit(app.exec_())