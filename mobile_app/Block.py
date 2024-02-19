#
#
#

# специальный импорт из директории srcкорневого каталога 
import sys
sys.path.append("../")
from src.logic import SpecialAction


from kivymd.uix.button import MDRaisedButton


class Block(MDRaisedButton):
    def __init__(self, text:str, **kwargs) -> None:
        super(Block, self).__init__(**kwargs)
        
        self.on_release = self.on_block_press
        self.text = text

    def on_block_press(self):
        print(f'Вы нажали на блок: {self.text}')
