from PyQt5.QtWidgets import QPushButton

import sys
sys.path.append("../")

from src.parse import parseData
from src.logic import SpecialAction


# кнопка переноса между вкладками зон
class ButtonConnectZones(QPushButton):
    def __init__(self, title: str):
        super().__init__()

        self.title = title.upper()

        # преобразование компонентов
        self.initUI()

    def initUI(self):
        # базовая инициализация
        self.setText(self.title)

        self.setStyleSheet("""
            background-color: #373737;
            background-position: center;
            height: 200%;
            width: 70%;
            min-width: 500px;
            min-height: 100px;
            
            color: #5CD561;
            font-size: 26px;
            font-weight: bold;
            
        """)

    def do(self, data):
        print(data)
        

# кнопка подключения к хостам
class ButtonConnect(QPushButton):
    def __init__(self, title: str):
        super().__init__()

        self.title = title

        # преобразование компонентов
        self.initUI()

    def initUI(self):
        # базовая инициализация
        self.setText(self.title)

        self.setStyleSheet("""
            background-color: #000000;
            background-position: center;
            color: #FFFFFF;
        """)

    def connect(self, user):
        '''
        
        '''
        
        print("OK")
        user, host = self.title.split("@")
        password = parseData("../data.json")["users"][user]

        self.ex = SpecialAction(user, host, password)



class ButtonActions(QPushButton):
    def __init__(self, title:str):
        super().__init__()

        self.title = title

        # преобразование компонентов
        self.initUI()

    def initUI(self):
        # базовая инициализация
        self.setText(self.title)

        self.setStyleSheet("""
            background-color: #000000;
            background-position: center;
            color: #FFFFFF;
        """)
        
    def runAction(self, action:int|str, **data) -> None:
        '''
        Выполнить дейтвие по укзанному номеру или по ключевому слову:
        
        - 1=on включить текущее устройство по технологии WakeOnLan
        
        - 2=off выключить текущее устройство через посыл команды `poweroff` или `shutdown -h now`

        - 3=openweb открыть браузер на текущем устройстве.
        Для окрытия используется дополнительные данные в виде словаря с данными, передаются в качестве обычного менованного аргумента.
        Вид должен быть: `{url="https://google.com"}`
        
        - 4=openapp открыть какое-то стороннее приложение на текущем устройстве. 
        Как и в случае с браузером необхзодимо передать дополнительные данные, а именно имя приложения и доп параметры (при необзодимости).
        К примеру: `{app="cura"}`
        
        - 5=send отправить на данное устройство какой-то файл и с использованием технологии SCP.
        В качестве дополнителньых параметров используются путь в какой каталог отправить файл.
        К примеру: {path="/home/student/Ivan/task", password="0000"} 
        
        - 6=audio управление звуком текущего устройства. В качесвте ожидаемых параметров требуется передать новое положение звука в процентах (от 0% до 100%)
        К примеру: {volume=100}
        '''
        
        if action == 1 or action.lower() == "on":
            self.on()
        
        elif action == 2 or action.lower() == "off":
            self.off()
            
        elif action == 3 or action.lower() == "openweb":
            self.openWeb(data)
            
        elif action == 4 or action.lower() == "openapp":
            self.openApp(data)
            
        elif action == 5 or action.lower() == "send":
            self.sendFile(data)
            
        elif action == 6 or action.lower() == "audio":
            self.changeVolume(data)
            
        

    def on(self):
        '''
        Включить текущий компьютер.
        '''
        
        print("Ключить компьютер")
        
    def off(self):
        '''
        Выключить текущий компьютер.
        '''
        
        print("Выключить компьютер")
        
    def openWeb(self, data):
        '''
        Открыть браузер с определенными параметрами. К примеру чтобы открыть веб браузер на странице google.com:
        data={'url'="https://google.com'}
        '''
        
        print("Отrрыть браузер")
        
    def openApp(self, data):
        '''
        Открыть установленное приложение с определенными параметрами. К примеру чтобы открыть приложение UltimakerCura:
        data={'app'="cura'}
        '''
        
        print("Открыть приложение")
        
    def sendFile(self, data):
        '''
        Отправить какой-то файл на теуущее устройство с использованием технологии `scp`.
        Для отправки требуется знать в какую дирректорию отправить файл и пароль пользователя, который получит файл.
        К примеру:
        data={'path'="/home/student/Ivan/task", password="0000"}
        '''
        
        print("Отпрвить файл")
        
    def changeVolume(self, data):
        '''
        Изменить громкость на текущем устройстве. громкость регулируется с использованием отдельного приложения звукозаписи `mixer`, 
        которое есть на большинстве Linux устройств. Ожидаемый параметр:
        data={'volume': 100}
        '''
        
        print("Громкость изменена!")