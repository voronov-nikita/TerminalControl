import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QLabel
import configparser
import json


config = configparser.ConfigParser()
config.read("config.ini")


TITLE:str = ""
JSON_FILE:str = ""





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())
