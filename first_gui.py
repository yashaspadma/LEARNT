import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First PyQt6 App")
        self.setGeometry(2800, 200, 300, 300)  # (x, y, width, height)

        layout = QVBoxLayout()

        label = QLabel("Hi, 6E")
        layout.addWidget(label)

        self.setLayout(layout)

app = QApplication(sys.argv)
window = SimpleApp()
window.show()
sys.exit(app.exec())
