# 
# 
# 
# 

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen


class MoreScreen(Screen):
    def update_data(self, data):
        self.data = data

    def on_back_button_press(self):
        app = MDApp.get_running_app()
        app.root.current = 'main_screen'