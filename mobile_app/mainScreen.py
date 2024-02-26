#
#
#
#

import sys
sys.path.append("../")


import threading
from Block import CustomButton
from src.parse import parseData, checkDevice

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp


# цвет кнопок хостов
BUTTON_COLOR: str = "#1F1F1F"
# цвет текста у кнопок подключения.
# Если устройство доступно, то BUTTON_TEXT_COLOR_TRUE иначе BUTTON_TEXT_COLOR_FALSE
BUTTON_TEXT_COLOR_TRUE: str = "1F9C2D"
BUTTON_TEXT_COLOR_FALSE: str = "A82D2E"


class MainScreen(Screen):
    # начальный массив состояний
    active = []

    def initHosts(self, addresses: list) -> list:
        '''
        Функция инициализирует состояние всех хостов в локальной сети.
        
        В качестве аргументов принимается только 
        массив с адресами компьютеров в локальной или глобальной сети.
        
        Массив должен формироваться через файл data.json, описанный выше в каталоге.
        
        В конечном итоге вернется другой массив (заполненый True и False),
        показывающие состояния конкретных компьютеров.
        '''
    
        results = []

        def worker(address):
            print(checkDevice(f"{address}.local"))
            results.append(checkDevice(address))

        #Подготовка потоков для каждого адреса
        threads = [threading.Thread(target=worker, args=(address,)) for address in addresses]
        
        # начинаем каждый поток
        for thread in threads: thread.start()
        # Дожидаемся завершения всех потоков
        for thread in threads: thread.join()
        return results


    def on_pre_enter(self) -> None:
        '''

        '''

        # инициализация хостов
        listHosts = parseData("../data.json")['Zones']["Zone3"]
        
        if not self.active:
            self.active = self.initHosts([elem['host'] for elem in listHosts.values()])

        # получаем объект сетчатого экрана
        grid_layout = self.ids.grid

        if not grid_layout.children:
            # индексатор для кнопок
            btn_number = 0
            for elem in listHosts.values():
                # парсим необходимый хост устройства
                hostname = elem['host']

                button = CustomButton(
                    text=f'Подключиться к {hostname}',
                    md_bg_color=BUTTON_COLOR,
                    text_color=(BUTTON_TEXT_COLOR_FALSE, BUTTON_TEXT_COLOR_TRUE)[
                        self.active[btn_number]]
                )
                button.bind(on_press=self.on_button_press)
                grid_layout.add_widget(button)
                # переходим к следующей кнопке в массиве
                btn_number += 1

    def on_button_press(self, button):
        '''

        '''
        ...
        
