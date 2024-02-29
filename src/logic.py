#
#
#
#


import wakeonlan
import paramiko


from threading import Thread


#
class Actions():
    def __init__(self, user: str, host: str, password: str) -> None:
        self.user = user
        self.host = host
        self.password = password

    def connect(self) -> None:
        '''
        Производиться подключение к удаленной машине. 
        Используюся те параметры, которые были переданы при инициализации экземпляра
        класса. 
        '''

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.ssh.connect(self.host, username=self.user, password=self.password)

    def exportDisplay(self) -> None:
        '''
        Экспорт виртуального экрана. Данная команда требуется для того, 
        чтобы можно было отображать в GUI интерфейсе Linux какие-либо изменения в 
        KDE облочке устройсва.
        '''

        self.ssh.exec_command("export DISPLAY=:0")

    def remotePrint(self, command: str) -> str:
        '''

        '''
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdout.read().decode('utf-8')

    def executeCommand(self, command: str, sudoPassword: str = None, output: bool = False) -> str | None:
        '''
        Ввыполнить команду. Функция позволяет выполнить переданную команду на удаленной машине.
        команда может быть любого характера, главное чтобы она поддерживалась технологией
        ssh. 

        В качестве первого аргумента примнимается сама команда, 
        затем sudo пароль при необходимости. В качестве 3-его аргумента ожидается булевый тип данных
        (т.е False(0) или True(1))
        Данный параметр отвечает за то, чтобы в терминал выводлась или не выводилась кака-ято информация,
        пришедшая из терминала удаленного компьютера.
        '''

        if sudoPassword is not None:
            stdin, stdout, stderr = self.ssh.exec_command(
                command, get_pty=True)
            stdin.write(sudoPassword+"\n")
            stdin.flush()
        else:
            stdin, stdout, stderr = self.ssh.exec_command(command)

        if output:
            return stdout.read().decode('utf-8')
        return


#
class SpecialAction(Actions):
    def __init__(self, user, host, password):

        super().__init__(user, host, password)

        self.connect()
        self.exportDisplay()

    def openWebBrowser(self, url: str, otherBrowser: str = "chromium-browser") -> None:
        '''
        Открыть веб браузер. 
        Данная команда буквально открывает браузер на удаленной машине.

        В качестве обязательного аргумента ожидвается url сайта, который нужно открыть.
        В качестве второго (не обязательного) аргумента ожидается приход названия приложения
        специфичного браузера.
        По умолчанию стоит браузер на движке хромиум - chromium-browser

        '''

        self.executeCommand(
            f"echo 'DISPLAY=:0 {otherBrowser} {url}' | at now")

    def turnOff(self) -> None:
        '''
        Выключить. 
        Команда выключает компьютер и заодно очищает кесь накопившийся кэш.
        '''

        self.executeCommand("poweroff")

    def reboot(self, sudoPassword: str) -> None:
        '''
        Перезагрузка.
        Команда перезагружает компьютер.
        '''

        self.executeCommand(f"sudo reboot", sudoPassword=sudoPassword)

    def sendFile(self, localFilePath: str, remoteFilePath: str) -> None:
        '''
        Отправить файл.
        Команда отправляет файл с локальной машины на удаленную.

        В качестве первого аргумента ожидаеться адрес файла, который необходимо отправить.

        В качестве второго аргумента ожидаеться путь удаленного хранения этого файла.

        '''

        scp = self.ssh.open_sftp()
        scp.put(localFilePath, remoteFilePath)
        scp.close()

    def WakeOnLan(self, macAddress: str) -> None:
        '''
        Включить по сети.

        Если компьютер подключен к локальной сети по беспроводному соединению, то 
        скорее всего ему доспно включение по сети.

        Это работает таким образом, чтобы по mac адресу узнать индификаор компьютера 
        и отправить ему магический пакет, который как раз его и разбудит.

        '''

        try:
            wakeonlan.send_magic_packet(macAddress)
            print(f"Magic packet sent to {macAddress}")
        except Exception as e:
            print(f"Error: {e}")

    def notify(self, message: str, sender: str, title: str) -> None:
        '''
        Уведомление.

        Функция вызывает системное уведомление
        '''

        self.executeCommand(f'''
                        echo "DISPLAY=:0 notify-send -a '{title}' '{sender}' '{message}'" | at now
                        ''')
                echo "DISPLAY=:0 notify-send -a '{title}' '{sender}' '{message}'" | at now
                ''')


def initConnect(user, host, password):
    # ex = SpecialAction(user, host, password)
    # ex.openWebBrowser("https://school.mos.ru")
    # ex.executeCommand("pkill -f chrome")
    ex.shutdown()


# тестирование функций
if __name__ == "__main__":
    ls = parseData("../data.json")["Zones"]["Zone5"]
    for i in range(3, 30):
        # wakeonlan.send_magic_packet(ls[str(i)]["mac"])
        try:
            ex = SpecialAction("student", f"sm1532-2-ip3-{i}.local", "1234")
            ex.turnOff()
            # ex = Thread(target=initConnect, args=(
            #     "student", f"sm1532-2-ip5-{i}.local", "1234"))
            # ex.start()
        except:
            print(f"Error:", i)
