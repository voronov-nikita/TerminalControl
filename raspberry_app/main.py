# 
# 
# 
# 


import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

from driver_ssh import driver, driver_sftp
from driver_wol import send_wol_packet


class ManagerSSHAppRaspPi(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI_raspberryPi.ui', self)

        # # Обновление списка возможных хостов
        self.hostsAll = self.getListHosts()

        # Выключить все хосты
        self.btnPowerOff.clicked.connect(self.startPoweroff)

        # Запустить все ПК
        self.btnWOL.clicked.connect(self.sendWOL)

        # Загрузить сайт на ПК
        self.btnDownloadSite.clicked.connect(self.sendSitePC)

        # Загрузить файл на ПК
        self.btnDownloadFile.clicked.connect(self.downloadFilePC)

    def startPoweroff(self):
        command = 'poweroff'
        driver(self.hostsAll, command)

    def sendWOL(self):
        mac_addresses = self.getListMacAddresses()
        for mac in mac_addresses:
            send_wol_packet(mac)

    def sendSitePC(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать файл с ссылкой', '')[0]
        with open(fname, 'r') as link_file:
            link = link_file.readline()
        command = f"export DISPLAY=:0; echo 'DISPLAY=:0 chromium-browser https://{link}' | at now"
        driver(self.hostsAll, command)
        print(link, command)

    def downloadFilePC(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать файл для загрузки', '')[0]
        driver_sftp(self.hostsAll, fname)
        print(fname)


    def getListHosts(self):
        with open('hosts_list.txt', 'r') as h:
            # hosts = list(map(lambda x: [x.rstrip(), self.pingHost(x.rstrip())], h.readlines()))
            hosts = list(map(lambda x: x.rstrip(), h.readlines()))
        return hosts

    def getListMacAddresses(self):
        with open('mac_addresses_zone3.txt', 'r') as m:
            mac_addresses = list(map(lambda x: x.rstrip(), m.readlines()))
        return mac_addresses




if __name__=="__main__":
    app = QApplication(sys.argv)
    managerAppRaspPi = ManagerSSHAppRaspPi()
    managerAppRaspPi.show()
    sys.exit(app.exec_())
