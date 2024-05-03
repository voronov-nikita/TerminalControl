#
# Устройсво на базе микрокомпьютера Raspberry pi 3B
# В файле описан исходный код приложения для точного управления всеми компьютерами в локальной сети
# Приложение написано на PyQt5 с использованием визуальных UI интерфесов xml формата
#


import sys

# добавим внешний путь для увеличения области видимости
sys.path.append("../")

from src.parse import parseData, WakeOnLan, checkDevice
# from src.logic import SpecialAction

from PyQt5.QtWidgets import *
from PyQt5 import uic



USER: str = "student"
PASSWORD: str = parseData("../data.json")['users'][USER]


class ManagerSSHAppRaspPi(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI_raspberryPi.ui', self)

        # # Обновление списка возможных хостов
        self.hostsAll = parseData("../data.json")['zones']

        # Выключить все хосты
        # self.btnPowerOff.clicked.connect(self.startPoweroff)

        # Запустить все ПК
        self.btnWOL.clicked.connect(self.enableAll)

        # Открыть сайт на всех ПК из списка хостов
        # self.btnDownloadSite.clicked.connect(self.sendSitePC)

        # Загрузить файл на ПК
        # self.btnDownloadFile.clicked.connect(self.downloadFilePC)

    # def startPoweroff(self):
    #     command = 'poweroff'
    #     driver(self.hostsAll, command)

    def enableAll(self):
        '''
        Функция включения всех данных из массива хостов. 
        
        Технология WakeOnLan.
        
        MAC адреса берутся из файла ```data.json```, хранящий в себе информацию о хостах.
        '''
        
        for mac in self.hostsAll['zone3']:
            WakeOnLan(mac['host'])

    # def sendSitePC(self):
    #     fname = QFileDialog.getOpenFileName(
    #         self, 'Выбрать файл с ссылкой', '')[0]
    #     with open(fname, 'r') as link_file:
    #         link = link_file.readline()
    #     command = f"export DISPLAY=:0; echo 'DISPLAY=:0 chromium-browser https://{
    #         link}' | at now"
    #     driver(self.hostsAll, command)
    #     print(link, command)

    # def downloadFilePC(self):
    #     fname = QFileDialog.getOpenFileName(
    #         self, 'Выбрать файл для загрузки', '')[0]
    #     driver_sftp(self.hostsAll, fname)
    #     print(fname)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    managerAppRaspPi = ManagerSSHAppRaspPi()
    managerAppRaspPi.show()
    sys.exit(app.exec_())
