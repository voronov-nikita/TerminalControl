import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QLabel, QStackedWidget
from PyQt5.QtGui import QColor

class ZoneInfoWidget(QWidget):
    def __init__(self, zone_data, main_window):
        super().__init__()
        self.zone_data = zone_data
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: black; color: green;")

        layout = QVBoxLayout()

        label = QLabel(self.zone_data['name'])
        layout.addWidget(label)

        for item in self.zone_data['items']:
            button = QPushButton(item)
            layout.addWidget(button)

        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.main_window.show_zones_list)
        layout.addWidget(back_button)

        self.setLayout(layout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Zones App')
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()

        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        self.listWidget = QListWidget()
        self.stacked_widget.addWidget(self.listWidget)

        self.listWidget.addItem("Zone 1")
        self.listWidget.addItem("Zone 2")

        self.listWidget.clicked.connect(self.on_zone_clicked)

        self.setLayout(self.main_layout)

        self.zone_info_widgets = []

    def on_zone_clicked(self, index):
        selected_zone = index.data()
        zone_data = {'name': selected_zone, 'items': ['Item 1', 'Item 2', 'Item 3']}
        self.show_zone_info(zone_data)

    def show_zone_info(self, zone_data):
        zone_info_widget = ZoneInfoWidget(zone_data, self)
        self.stacked_widget.addWidget(zone_info_widget)
        self.stacked_widget.setCurrentWidget(zone_info_widget)
        self.zone_info_widgets.append(zone_info_widget)

    def show_zones_list(self):
        for widget in self.zone_info_widgets:
            self.stacked_widget.removeWidget(widget)
        self.stacked_widget.setCurrentWidget(self.listWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
