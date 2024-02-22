from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build()

    def build(self):
        self.layout = self.create_layout()
        self.add_widget(self.layout)

    def create_layout(self):
        layout = MDBoxLayout(orientation="vertical", spacing=10)

        for i in range(20):
            btn = MDRaisedButton(
                text=f'Button {i}',
                on_release=self.on_button_click,
                size_hint=(1, None),
                height=60,
                md_bg_color=(0.2, 0.2, 0.2, 1),
            )
            layout.add_widget(btn)

        return layout

    def on_button_click(self, instance):
        app = MDApp.get_running_app()
        app.screen_manager.transition = SlideTransition(direction="left")
        app.screen_manager.switch_to(OtherScreen())

class OtherScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build()

    def build(self):
        self.layout = self.create_layout()
        self.add_widget(self.layout)

    def create_layout(self):
        layout = MDBoxLayout(orientation="vertical", spacing=10)

        for i in range(20):
            btn = MDRaisedButton(
                text=f'Other Button {i}',
                on_release=self.on_button_click,
                size_hint=(1, None),
                height=60,
                md_bg_color=(0.2, 0.2, 0.2, 1),
            )
            layout.add_widget(btn)

        return layout

    def on_button_click(self, instance):
        app = MDApp.get_running_app()
        app.screen_manager.transition = SlideTransition(direction="right")
        app.screen_manager.switch_to(HomeScreen())

class ScrollableListApp(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()

        # Добавляем начальный экран (HomeScreen)
        home_screen = HomeScreen(name="home_screen")
        self.screen_manager.add_widget(home_screen)

        return self.screen_manager

if __name__ == '__main__':
    ScrollableListApp().run()
