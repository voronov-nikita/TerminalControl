
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QDesktopWidget
from OneZoneWidget import OneZoneInfo
import configparser
import json
import sys


config = configparser.ConfigParser()
config.read("config.ini")

SIZE_APP: tuple = eval(config['App'].get('size'))
TITLE: str = config['App'].get('title')
JSON_FILE: str = config['App'].get('file')



class MainApp(QWidget):
    def __init__(self) -> None:
        '''

        '''

        super().__init__()

        # работа с загрузочной информацией (название, положение)
        self.setWindowTitle(TITLE)
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

        self.listWidget = QListWidget()
        self.mainLayout.addWidget(self.listWidget)

        with open(JSON_FILE) as file:
            data = json.load(file)
            for name in data['zones'].keys():
                self.listWidget.addItem(name)

        self.listWidget.clicked.connect(self.on_zone_clicked)

        self.setLayout(self.mainLayout)

    def on_zone_clicked(self, index):
        
        selected_zone = index.data()
        print(selected_zone)
        
        with open(JSON_FILE) as file:
            data = json.load(file)
            for zone in data['zones'].keys():
                if zone == selected_zone:
                    # списко имен хостов
                    hosts = [data['zones'][zone][i]['host'] for i in data['zones'][zone]]
                    self.show_zone_info(hosts)

    def show_zone_info(self, zone_data):
        # Очищаем текущий макет
        for i in reversed(range(self.mainLayout.count())):
            widget = self.mainLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Создаем новый виджет с информацией о зоне и добавляем его к основному макету
        zone_info_widget = OneZoneInfo(zone_data)
        self.mainLayout.addWidget(zone_info_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())
