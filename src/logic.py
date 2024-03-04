#
# Файл, описывающий логику действий базовых команд.
# Здесь же хранится класс, описыващий все действия для конкретной машины.
# К примеру выключить компьютер или перезагруз его через удаленный доступ.
#
#

from parse import parseData, checkDevice, WakeOnLan

import paramiko


from threading import Thread


# Класс базовых действий
# Описывает состояниеподключения и работу конкретно с оборудованием оболочки Linux системы
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
        Метод, способный отобразить в собвтенном терминале подключающегося информацию
        из терминала удаленной машины. 

        - command - команда, которая должны выполниться на удаленной машине.

        В консоле админимтратора отобразиться информация, которая должна отобразиться 
        на удаленном компьютере. 

        К примеру при вызове метода ```remotePrint(command="ls")``` в терминале отобразится
        то, что хранится на удаленной машине в формате списка со всеми скрытыми эллементами при вызове совместно с атрибутом ```r''```
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


# Класс специальных действий
# Открытие бразуера на удаленной машине, выключение питания, отправка файла и многое другое.
class SpecialAction(Actions):
    def __init__(self, user, host, password):

        super().__init__(user, host, password)

        # произвести подключение и экспорт удаленного дисплея для работы с id процессами
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

    def shutdown(self) -> None:
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

    def notify(self, message: str, sender: str, title: str) -> None:
        '''
        Уведомление.

        Функция вызывает системное уведомление. 
        Для уведомленения необходимо передать несколько параметров:

        - message - само сообщение, которое будет передаваться в качестве
        основного блока;

        - sender - имя отправителя. Это отображаемое имя приложения или 
        какого-либо пользователя в синформации о сообщении;

        - title - заголовок сообщения. 
        Отображаемая информация о заголовке информации. Это самое большое, что отображается в уведомлении.
        '''

        self.executeCommand(f'''
                echo "DISPLAY=:0 notify-send -a '{title}' '{sender}' '{message}'" | at now
                ''')


def start(user, host, password):
    ex = SpecialAction(user, host, password)
    # ex.openWebBrowser("https://school.mos.ru")
    # ex.executeCommand("pkill -f chrome")
    ex.shutdown()


# тестирование функций
if __name__ == "__main__":
    ls = parseData("../data.json")["zones"]["zone5"]
    print(ls)
    for i in range(1, 13):
        WakeOnLan(ls[str(i)]['mac'])
        # try:
        #     ex = Thread(target=start, args=(
        #         "student", f"sm1532-2-ip5-{i}.local", "1234"))
        #     ex.start()
        # except:
        #     print(f"Error:", i)
