
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QDesktopWidget, \
    QStackedWidget, QScrollArea
from PyQt5.QtGui import QIcon

from OneZoneWidget import OneZoneInfo

import configparser
import json
import sys


config = configparser.ConfigParser()
config.read("config.ini")

SIZE_APP: tuple = eval(config['App'].get('size'))
TITLE: str = config['App'].get('title')
JSON_FILE: str = config['App'].get('file')
ICON :str = config['App'].get('icon')


class MainApp(QWidget):
    def __init__(self) -> None:
        '''

        '''

        super().__init__()

        # работа с загрузочной информацией (название, положение)
        self.setWindowTitle(TITLE)
        self.setWindowIcon(QIcon(ICON))
        self.setGeometry(100, 100, 400, 300)
        self._center()

        self.initUI()

    def _center(self) -> None:
        '''
        Отцентрить текущее окно отночительно экрана.
        '''

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2,
                  (screen.height() - size.height()) // 2)

    def initUI(self) -> None:
        '''
        Инициализация пользовательского интерфейса.
        '''

        self.mainLayout = QVBoxLayout()

        self.stackedWidget = QStackedWidget()
        self.mainLayout.addWidget(self.stackedWidget)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        self.listWidget = QListWidget()

        # добавляем элементы первого уровня (самого верхнего) в json в качестве кнопок
        with open(JSON_FILE) as file:
            data = json.load(file)
            for name in data['zones'].keys():
                self.listWidget.addItem(name)

        self.listWidget.clicked.connect(self.onZoneClicked)

        self.scrollArea.setWidget(self.listWidget)
        self.stackedWidget.addWidget(self.scrollArea)

        self.setLayout(self.mainLayout)

        # массив с сохранением последовательности действий
        self.zoneInfoWidgets = []

    def onZoneClicked(self, index) -> None:
        '''
        Начать обработку оторажения списка данных из конкретной зоны.
        '''

        selected_zone = index.data()

        with open(JSON_FILE) as file:
            data = json.load(file)
            for zone in data['zones'].keys():
                if zone == selected_zone:
                    # списко имен хостов в этой зоне
                    hosts = [data['zones'][zone][i]['host'] for i in data['zones'][zone]]
                    self.show_zone_info(zone, hosts)

    def show_zone_info(self, title: str, dataList: list) -> None:
        '''
        Отредактировать текущий эран на новый путем создания новго экземпляра класса.
        '''

        # Создаем новый виджет с информацией о зоне и добавляем его к основному макету
        zone_info_widget = OneZoneInfo(title, dataList, self)

        self.stackedWidget.addWidget(zone_info_widget)
        self.stackedWidget.setCurrentWidget(zone_info_widget)
        self.zoneInfoWidgets.append(zone_info_widget)

    def showHome(self) -> None:
        '''
        Изменить текущее активный эллемент на новый или предыдущий из массива последовательности действий.
        '''

        for widget in self.zoneInfoWidgets:
            self.stackedWidget.removeWidget(widget)
        self.stackedWidget.setCurrentWidget(self.listWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())
