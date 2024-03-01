from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton
from kivy.uix.boxlayout import BoxLayout

class MyApp(MDApp):
    def build(self):
        self.screen = MDScreen()

        # Создаем BoxLayout для центрирования
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Создаем кнопку с встроенной иконкой и устанавливаем размер иконки
        icon_button = MDIconButton(icon="android", pos_hint={'center_x': 0.5, 'center_y': 0.5})
        icon_button.bind(on_release=self.icon_button_pressed)
        
        # Добавляем кнопку в BoxLayout
        layout.add_widget(icon_button)

        # Добавляем BoxLayout на экран
        self.screen.add_widget(layout)

        return self.screen

    def icon_button_pressed(self, instance):
        print("IconButton pressed.")

MyApp().run()
