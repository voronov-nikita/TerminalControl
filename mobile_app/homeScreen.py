

from src.parse import parseData

from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp


class HomeScreen(Screen):
    def on_pre_enter(self):
        
        # инициализация хостов
        listZones = parseData("../data.json")['zones']
        
        
        # получаем объект сетчатого экрана
        grid_layout = self.ids.grid2

        if not grid_layout.children:
            # индексатор для кнопок
            for elem in listZones.keys():
                button = MDRaisedButton(
                        text=str(elem)
                    )
                grid_layout.add_widget(button)
            
            button1 = MDRaisedButton(text="Laptops")
            grid_layout.add_widget(button1)
            
            button2 = MDRaisedButton(text="All")
            grid_layout.add_widget(button2)
    
    
    def on_back_button_press(self):
        print("OK")



if __name__=="__main__":
    pass