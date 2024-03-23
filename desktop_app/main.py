#
# Основной файл загрузки приложения
# Здесь происходит инициализация основных параметров и компонентов, включая отдельные вкладки и страницы приложения
# Хранение временных данных и обработка переходов расположены между взаимосвязями
#

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

import sys

from HomePage import Home


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.setGeometry(0, 0, 600, 600)

        # Создаем виджеты для различных страниц
        btn = QPushButton("На страницу 2", self, clicked=self.switch_to_page2)
        self.page1 = Home(btn)
        
        
        self.page2 = QWidget()
        self.page2_layout = QVBoxLayout(self.page2)
        self.page2_layout.addWidget(QPushButton("На страницу 1", self, clicked=self.switch_to_page1))

        # Добавляем страницы в QStackedWidget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        # Главное окно
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.stacked_widget)

        
    def switch_to_page1(self):
        self.stacked_widget.setCurrentIndex(0)

    def switch_to_page2(self):
        self.stacked_widget.setCurrentIndex(1)

        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    instance = MyApp()
    instance.show()
    sys.exit(app.exec_())
