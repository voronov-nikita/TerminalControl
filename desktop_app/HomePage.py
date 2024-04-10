#
# Файл, описывающий зависимости в окне №1 приложения
# В окне "Дом" назодятся основные кнопки, подктверждения, хранения и фильтрации данных
# Зависимости для описания логики подключения, хранения и транспортировки не требуются
#

from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
import sys

sys.path.append("../")

from src.parse import parseData
from Components import ButtonConnectZones


# Класс, в котором описаны зависимости для базовых кнопок при автовходе
class Home(QWidget):
    def __init__(self):
        super().__init__()
        
        self.listButtons = parseData("../data.json")['zones']
        
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

        self.page1_layout = QVBoxLayout(self)
        
        for i in self.listButtons:
            button = ButtonConnectZones(str(i))
            button.clicked.connect(lambda _, arg=i: button.do(arg))
            self.page1_layout.addWidget(button)
        
        # Конпка для одновременного подлючения ко всем 
        button = ButtonConnectZones("ALL DEVICE")
        button.clicked.connect(lambda _, arg="ALL": button.do(arg))
        self.page1_layout.addWidget(button)
        


# Для тестрования отдельного блока используется данная конструкция
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Home()
    ex.show()
    sys.exit(app.exec_())
