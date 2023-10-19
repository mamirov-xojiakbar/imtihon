from PyQt6.QtWidgets import (QLineEdit, QLabel, QPushButton, QWidget, QPlainTextEdit,
                              QMainWindow, QVBoxLayout)

class NewWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Imtihon savol')
        self.main_layout = QVBoxLayout()
        self.add_widget()
        self.setCentralWidget(self.main_widget)

    def add_widget(self):
        self.input_city = QPlainTextEdit()
        self.text_edit = QLineEdit()
        self.response_button = QPushButton('result')
        self.result = QLabel()
        
        self.main_layout.addWidget(self.input_city)
        self.main_layout.addWidget(self.text_edit)
        self.main_layout.addWidget(self.result)
        self.main_layout.addWidget(self.response_button)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.response_button.clicked.connect(self.count)
        self.result.hide()

    def count(self):
        cnt = self.input_city.toPlainText().count(self.text_edit.text())
        self.result.setText(str(cnt))
        self.result.show()