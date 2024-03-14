from PyQt5.QtWidgets import QPushButton

import sys
sys.path.append("../")

from src.parse import parseData
from src.logic import SpecialAction


class ButtonConnect(QPushButton):
    def __init__(self, title: str):
        super().__init__()

        self.title = title

        # базовая инициализация
        self.setText(self.title)

        self.setStyleSheet("""
            background-color: #000000;
            background-position: center;
        """)

        # преобразование компонентов
        self.initUI()

    def initUI(self):
        pass

    def connect(self, user):
        user, host = self.title.split("@")
        password = parseData("../data.json")["users"][user]

        self.ex = SpecialAction(user, host, password)
