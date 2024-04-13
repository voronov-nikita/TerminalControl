from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication,\
    QListWidget, QListWidgetItem, QScrollArea
import sys

sys.path.append("../")


class OneZoneInfo(QWidget):
    def __init__(self, title:str, data: list, mainWindow:QWidget) -> None:
        '''
        
        '''
        
        super().__init__()

        self.title = title
        self.data = data
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
        for elem in self.data:
            button = QPushButton(elem)
            button.clicked.connect(lambda: print("OK"))
            
            item = QListWidgetItem()
            
            self.lsWidget.addItem(item)
            self.lsWidget.setItemWidget(item, button)
        
        # кнопка назад
        item = QListWidgetItem()
        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.mainWindow.showHome)
        self.lsWidget.addItem(item)
        self.lsWidget.setItemWidget(item, back_button)
        
        
        layout.addWidget(self.lsWidget)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OneZoneInfo()
    ex.show()
    sys.exit(app.exec_())
