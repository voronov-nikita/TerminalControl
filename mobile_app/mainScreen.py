#
#
#
#

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp

import sys
sys.path.append("../")

from src.parse import parseData


from Block import CustomButton


BUTTON_COLOR:str = "#1F1F1F"


class MainScreen(Screen):
    
    
    
    def on_pre_enter(self):
        '''
        
        '''
        
        listHosts = parseData("../data.json")['Zones']["Zone3"]
        
        # получаем объект сетчатого экрана
        grid_layout = self.ids.grid
        
        if not grid_layout.children:
            
            for elem in listHosts.values():
                button = CustomButton(
                        text=f'Подключиться к {elem['host']}',
                        md_bg_color = BUTTON_COLOR
                    )
                button.bind(on_press=self.on_button_press)
                grid_layout.add_widget(button)

    def on_button_press(self, button):
        '''
        
        '''
        # Изменяем цвет текста кнопки на красный
        button.theme_text_color = "Custom"
        button.md_bg_color = (1, 0, 0, 1)
