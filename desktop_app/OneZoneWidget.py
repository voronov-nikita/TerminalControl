from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication,\
    QListWidget, QListWidgetItem, QStackedWidget
import sys

from OneHostWidget import MoreAction

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
        
        self.lsWidget = QListWidget()
        
        self.stackedWidget = QStackedWidget()
        layout.addWidget(self.stackedWidget)
        
        # добавляем все кнопки из массива хостов
        for elem in self.data:
            button = QPushButton(elem)
            button.clicked.connect(self.show_host_action)
            
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
        
        self.zoneInfoWidgets = []
        
    def show_host_action(self) -> None:
        '''
        Отредактировать текущий эран на новый путем создания новго экземпляра класса.
        '''

        # Создаем новый виджет с информацией о зоне и добавляем его к основному макету
        newWidget = MoreAction(title=self.title, mainWindow=self)

        self.stackedWidget.addWidget(newWidget)
        self.stackedWidget.setCurrentWidget(newWidget)
        self.zoneInfoWidgets.append(newWidget)
        
    def showHome(self) -> None:
        '''
        Изменить текущее активный эллемент на новый или предыдущий из массива последовательности действий.
        '''

        for widget in self.zoneInfoWidgets:
            self.stackedWidget.removeWidget(widget)
        self.stackedWidget.setCurrentWidget(self.lsWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OneZoneInfo()
    ex.show()
    sys.exit(app.exec_())