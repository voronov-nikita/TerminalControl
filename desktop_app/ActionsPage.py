from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
import sys

from Components import ButtonActions


class Actions(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.windowSize:tuple = (800, 600)
        self.title:str = "Terminal Control"
        self.icon:str = "../assets/mainIcon.jpg"
        
        self.initHead()
        self.initUI()
        
        
    def _center(self):
        '''
        Функция выравнивания всего окна относительно текущего экрана.
        '''
        
        screen = QDesktopWidget().screenGeometry()

        size = self.geometry()
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        self.move(x, y)
        

    def initHead(self) -> None:
        '''
        Функция, которая используется при инициализации класса ```Home```
        
        Используется для инициализации головных параметров окна, такие как:
        
        - Размеры окна
        - Название окна
        - Геометрия окна
        
        И другое.
        '''
        
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))
        self.setGeometry(0, 0, *self.windowSize)
        self._center()
        
        # установка стиля для окна приложения
        self.setStyleSheet("""
            background-color: #181818;
        """)

    def initUI(self) -> None:
        '''
        Функция, которая используется при инициализации класса ```Home```
        
        Используется для инициализации пользовательских параметров окна, такие как:
        
        - Кнопки приложения
        - Все лэйауты активного окна
        - Текстовые части
        - Инициализация списка
        
        И другое.
        '''

        layout = QVBoxLayout(self)
        
        button_wakeonlan = ButtonActions(title="Выколючить компьютер")
        
        self.setLayout(layout)