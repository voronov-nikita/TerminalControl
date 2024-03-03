import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QFileDialog, QDesktopWidget
from PyQt5.QtGui import QIcon

class AddDataDialog(QDialog):
    def __init__(self, parent=None):
        super(AddDataDialog, self).__init__(parent)
        self.setWindowTitle('Добавление данных в JSON')
        self.setGeometry(100, 100, 400, 200)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel('Введите данные:')
        self.data_input = QLineEdit()

        buttons_layout = QHBoxLayout()
        ok_button = QPushButton('OK', self)
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton('Отмена', self)
        cancel_button.clicked.connect(self.reject)

        buttons_layout.addWidget(ok_button)
        buttons_layout.addWidget(cancel_button)

        layout.addWidget(label)
        layout.addWidget(self.data_input)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 600, 400)
        self.center()

        self.setWindowTitle('Центральное окно')

        # Создаем кнопку с иконкой "+"
        add_button = QPushButton(QIcon('plus_icon.png'), '', self)
        add_button.setGeometry(self.width() - 50, self.height() - 50, 40, 40)
        add_button.clicked.connect(self.showAddDataDialog)

        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        self.move(x, y)

    def showAddDataDialog(self):
        dialog = AddDataDialog(self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            data = dialog.data_input.text()
            with open("test.json", 'w') as file:
                file.write(f"'test1':'{data}'")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
