from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QLabel, QBoxLayout, QApplication
from Components import ButtonConnect

import sys
sys.path.append("../")

from src.parse import parseData

class MainContent(QWidget):
    def __init__(self):
        super().__init__()

        # собираем данные для формирования списка кнопок и зон
        self.data = parseData("../data.json")

        self.initUI()

    def initUI(self):
        # основное тело сбора данных
        layout = QVBoxLayout(self)

        self.scroll_area = QScrollArea()

        self.box = QVBoxLayout(self)
        for i in range(10):
            self.box.addWidget(ButtonConnect(f"Кнопка {i}"))
        
        self.scroll_area.setWidget(self.box)
        layout.addWidget(self.scroll_area)


# Для тестрования отдельного блока используется данная конструкция
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainContent()
    ex.show()
    sys.exit(app.exec_())
