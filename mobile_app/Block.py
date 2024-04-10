from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
    
class CustomButton(MDRaisedButton):
        
    def on_press(self):
        app = MDApp.get_running_app()
        data_to_pass = "Привет, я данные с предыдущего экрана!"
        app.root.current = 'more_screen'
        app.root.get_screen('more_screen').update_data(data_to_pass)
        # Вызываем оригинальный метод on_press родительского класса MDRaisedButton
        super(CustomButton, self).on_press()
        
        
        
class HomeButtons(MDRaisedButton):
        
    def on_press(self):
        app = MDApp.get_running_app()
        data_to_pass = "Привет, я данные с предыдущего экрана!"
        app.root.current = 'more_screen'
        app.root.get_screen('more_screen').update_data(data_to_pass)
        # Вызываем оригинальный метод on_press родительского класса MDRaisedButton
        super(CustomButton, self).on_press()
        
    