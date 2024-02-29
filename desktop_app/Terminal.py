import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QVBoxLayout, QPushButton, QWidget, QProcess

class TerminalWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Terminal App")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.terminal_output = QPlainTextEdit(self)
        self.layout.addWidget(self.terminal_output)

        self.input_button = QPushButton("Run Command", self)
        self.input_button.clicked.connect(self.run_command)
        self.layout.addWidget(self.input_button)

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.update_output)

    def run_command(self):
        command = "your_command_here"
        self.process.start(command)

    def update_output(self):
        output = self.process.readAllStandardOutput()
        self.terminal_output.appendPlainText(str(output, encoding='utf-8').strip())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TerminalWindow()
    window.show()
    sys.exit(app.exec_())
