# 
# 
# 
# 

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout

from mainScreen import MainScreen
from moreScreen import MoreScreen
from homeScreen import HomeScreen

Builder.load_file("main.kv")



class TerminalControl(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        
        sm = ScreenManager(transition=WipeTransition())

        # Добавление экранов в ScreenManager
        home_screen = HomeScreen(name="home_screen")
        menu_screen = MainScreen(name='main_screen')
        new_screen = MoreScreen(name='more_screen')

        sm.add_widget(home_screen)
        sm.add_widget(menu_screen)
        sm.add_widget(new_screen)

        return sm
    
    
if __name__=="__main__":
    TerminalControl().run()