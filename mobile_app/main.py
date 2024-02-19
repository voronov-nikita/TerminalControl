from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout, BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from Block import Block


Builder.load_string("""
#:import colors kivymd.color_definitions

<Block>:
    size_hint: None, None
    size: "150dp", "150dp"
    theme_text_color: "Custom"
    text_color: 1, 1, 1, 1  # Белый цвет текста
    md_bg_color: 0, 0, 0, 1  # Цвет фона

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
        Block:
            text: 'Блок 1'
            on_release: app.root.current = 'block1_screen'
        Block:
            text: 'Блок 2'
            on_release: app.root.current = 'block2_screen'
        Block:
            text: 'Блок 3'
            on_release: app.root.current = 'block3_screen'

<Block1Screen>:
    name: 'block1_screen'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Это уникальная часть для Блока 1'
        Button:
            text: 'Вернуться на главный экран'
            on_release: app.root.current = 'main'

<Block2Screen>:
    name: 'block2_screen'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Это уникальная часть для Блока 2'
        Button:
            text: 'Вернуться на главный экран'
            on_release: app.root.current = 'main'

<Block3Screen>:
    name: 'block3_screen'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Это уникальная часть для Блока 3'
        Button:
            text: 'Вернуться на главный экран'
            on_release: app.root.current = 'main'
""")

# Класс для главного экрана
class MainScreen(Screen):
    pass

# Классы для уникальных частей каждого блока
class Block1Screen(Screen):
    pass

class Block2Screen(Screen):
    pass

class Block3Screen(Screen):
    pass

# Основной класс приложения
class MyApp(MDApp):
    def build(self):
        # Создаем ScreenManager и добавляем экраны
        screen_manager = ScreenManager()

        main_screen = MainScreen()
        block1_screen = Block1Screen()
        block2_screen = Block2Screen()
        block3_screen = Block3Screen()

        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(block1_screen)
        screen_manager.add_widget(block2_screen)
        screen_manager.add_widget(block3_screen)

        return screen_manager


if __name__ == '__main__':
    MyApp().run()