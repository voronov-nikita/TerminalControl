from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

Builder.load_string("""
#:import colors kivymd.color_definitions

<Block>:
    size_hint: None, None
    size: "150dp", "150dp"
    theme_text_color: "Custom"
    text_color: 0, 1, 1, 1  # Белый цвет текста
    md_bg_color: 0, 0, 0, 1  # Цвет фона

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
        bg_color: 0, 0, 0, 1
        Block:
            text: 'block1'
        Block:
            text: 'block2'
        Block:
            text: 'block3'

<Block1Screen>:
    name: 'block1_screen'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Это уникальная часть для Блока 1'
        Button:
            text: 'Вернуться на главный экран'
            on_release: app.root.transition.direction = 'right'; app.root.current = 'main'

<Block2Screen>:
    name: 'block2_screen'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Это уникальная часть для Блока 2'
        Button:
            text: 'Вернуться на главный экран'
            on_release: app.root.transition.direction = 'right'; app.root.current = 'main'

<Block3Screen>:
    name: 'block3_screen'
    BoxLayout:
        orientation: 'vertical'
        background_color: 1, 0, 1, 1
        Label:
            text: 'Это уникальная часть для Блока 3'
            color: 0, 1, 1, 1
        Button:
            text: 'Вернуться на главный экран'
            on_release: app.root.transition.direction = 'right'; app.root.current = 'main'
""")

# Класс представляющий блок
class Block(MDRaisedButton):
    def __init__(self, **kwargs):
        super(Block, self).__init__(**kwargs)
        self.on_release = self.on_block_press

    def on_block_press(self):
        app = MDApp.get_running_app()
        app.root.transition.direction = 'left'
        app.root.current = f'{self.text.lower()}_screen'

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
        screen_manager = ScreenManager(transition=SlideTransition())

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
