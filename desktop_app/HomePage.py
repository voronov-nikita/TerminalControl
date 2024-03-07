#
# Файл, описывающий зависимости в окне №1 приложения
# В окне "Дом" назодятся основные кнопки, подктверждения, хранения и фильтрации данных
# Зависимости для описания логики подключения, хранения и транспортировки не требуются
#

from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon
import sys

# Класс, в котором описаны зависимости для базовых кнопок при автовходе
class Home(QWidget):
    def __init__(self, button):
        super().__init__()
        
        self.windowSize:tuple = (900, 700)
        self.title:str = "Terminal Control"
        self.icon:str = "../assets/mainIcon.jpg"
        
        self.initHead()
        self.initUI(button)
        
        
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

    def initUI(self, button) -> None:
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
        lbl = QLabel(self)
        lbl.setText("HOME")
        self.page1_layout.addWidget(lbl)
        self.page1_layout.addWidget(button)



# Для тестрования отдельного блока используется данная конструкция
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Home()
    ex.show()
    sys.exit(app.exec_())
