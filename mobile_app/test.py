from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.toolbar import MDTopAppBar
# from kivymd.uix.tabbedpanel import MDTabs
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen


class ComputerTab(MDBoxLayout, MDTabsBase):
    pass


class ComputerApp(MDApp):
    def build(self):
        return Builder.load_string(
            """
BoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Computer Control"
        elevation: 10

    MDTabs:
        id: tabs
"""

        )

    def on_start(self):
        for i in range(1, 6):  # Создаем 5 вкладок для компьютеров
            tab = ComputerTab(text=f"Компьютер {i}")
            tab.bind(on_tab_press=self.on_tab_press)
            self.root.ids.tabs.add_widget(tab)

    def on_tab_press(self, instance_tabs, instance_tab):
        self.root.ids.tabs.switch_tab(instance_tab)

        # Создаем вторую вкладку с действиями
        actions_tab = MDScreen(name=f"tab_{instance_tab.title}")

        # Добавляем кнопки на вторую вкладку
        actions_tab.add_widget(MDRaisedButton(text="Выключить/Включить"))
        actions_tab.add_widget(MDRaisedButton(text="Отправить файл"))
        actions_tab.add_widget(MDRaisedButton(text="Скачать"))
        actions_tab.add_widget(MDRaisedButton(text="Открыть браузер"))

        # Добавляем вторую вкладку в MDTabs
        self.root.ids.tabs.add_widget(actions_tab)


ComputerApp().run()
