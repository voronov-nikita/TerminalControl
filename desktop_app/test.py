import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.pages = [
            {"title": "Page 1", "content": "Content of Page 1"},
            {"title": "Page 2", "content": "Content of Page 2"},
            {"title": "Page 3", "content": "Content of Page 3"}
        ]

        self.current_page_index = 0

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("List Navigation")

        layout = QVBoxLayout(self)

        self.scroll_area = QScrollArea()
        layout.addWidget(self.scroll_area)

        content_widget = QWidget()
        self.scroll_area.setWidget(content_widget)
        self.scroll_area.setWidgetResizable(True)

        content_layout = QVBoxLayout(content_widget)

        for page in self.pages:
            button = QPushButton(page["title"])
            button.clicked.connect(lambda checked, title=page["title"]: self.change_page(title))
            button.setFlat(True)  # Убираем обводку у кнопки
            content_layout.addWidget(button)

        self.page_label = QLabel()
        content_layout.addWidget(self.page_label)

        self.update_page()

    def change_page(self, title):
        for index, page in enumerate(self.pages):
            if page["title"] == title:
                self.current_page_index = index
                self.update_page()
                break

    def update_page(self):
        page = self.pages[self.current_page_index]
        self.page_label.setText(page["content"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec_())
