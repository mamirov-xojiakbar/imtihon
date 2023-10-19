from sys import argv
from PyQt6.QtWidgets import (QLineEdit, QLabel, QPushButton, QWidget, 
                              QMainWindow, QVBoxLayout, QHBoxLayout, QCheckBox, QApplication)
from weather_api import weather

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('weather')
        self.main_layout = QVBoxLayout()
        self.add_widget()
        self.setCentralWidget(self.main_widget)

    # add widgets
    def add_widget(self):
        # the first line
        self.input_city = QLineEdit()
        
        # the second line
        self.CBox = QCheckBox()
        self.CBox.setText('celsius')
        self.KBox = QCheckBox()
        self.KBox.setText('kelvin')
        self.check_layout = QHBoxLayout()
        self.check_layout.addWidget(self.CBox)
        self.check_layout.addWidget(self.KBox)
        
        # the third line
        self.response_button = QPushButton('result')
        self.response_button.clicked.connect(self.weather_)
        
        # the fourth result line
        self.result = QLabel()
        self.result.setText('there should be something')
        
        # adding to main_layout
        self.main_layout.addWidget(self.input_city)
        self.main_layout.addLayout(self.check_layout)
        self.main_layout.addWidget(self.response_button)
        self.main_layout.addWidget(self.result)

        # Create main widget and assign the layout
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        
    # about weather
    def weather_(self):
        data = weather(self.input_city.text())
        temp = f"{data['temp']} kelvin"
        if self.CBox.isChecked():
            temp = f"{data['temp']-273.15} celsius"
        
        
        text = f"weather condition: {data['description']}\nweather: {temp}\nhumidity: {data['humidity']}\nwind speed: {data['wind']} m/s"
        
        self.result.setText(text)

