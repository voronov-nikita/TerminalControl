from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication
import sys

sys.path.append("../")


class OneZoneInfo(QWidget):
    def __init__(self, title:str, data: list) -> None:
        '''
        
        '''
        
        super().__init__()

        self.title = title
        self.data = data

        self.initUI()

    def initUI(self) -> None:
        '''

        '''

        layout = QVBoxLayout()

        label = QLabel(self.title)
        layout.addWidget(label)

        for item in self.data:
            button = QPushButton(item)
            layout.addWidget(button)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OneZoneInfo()
    ex.show()
    sys.exit(app.exec_())
