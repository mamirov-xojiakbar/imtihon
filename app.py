from PyQt6.QtWidgets import QApplication
from sys import argv 
from weather_pr import MainWindow

# ---main---
my_app = QApplication(argv)
window = MainWindow()
window.show()
my_app.exec()