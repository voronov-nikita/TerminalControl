from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import TwoLineListItem

KV = '''
BoxLayout:
    orientation: 'vertical'

    ScrollView:
        MDList:
            id: list_items

    MDRaisedButton:
        text: 'Добавить элемент'
        on_release: app.add_item()

<SecondScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        MDRaisedButton:
            text: 'Вернуться на первый экран'
            on_release: app.switch_screen()
'''


class SecondScreen(MDScreen):
    pass


class MyApp(MDApp):
    def build(self):
        self.screen_manager = Builder.load_string(KV)
        self.sm = ScreenManager()
        return self.screen_manager

    def add_item(self):
        list_items = self.screen_manager.ids.list_items
        item_text = f'Элемент {len(list_items.children) + 1}'
        
        # Создаем кнопку вместо TwoLineListItem
        button = MDRaisedButton(text=item_text, on_release=self.switch_to_second_screen)
        list_items.add_widget(button)

    def switch_to_second_screen(self, instance):
        # Переключение на второй экран
        # self.screen_manager.transition.direction = 'left'
        self.screen_manager.add_widget(SecondScreen(name='second_screen'))
        self.screen_manager.current = 'second_screen'

    def switch_screen(self):
        # Переключение на первый экран
        self.sm.transition.direction = 'right'
        self.sm.remove_widget(self.screen_manager.get_screen('second_screen'))
        self.sm.current = 'main_screen'


if __name__ == '__main__':
    MyApp().run()
