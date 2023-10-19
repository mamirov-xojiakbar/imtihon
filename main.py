from PyQt6.QtWidgets import QApplication
from sys import argv
from new import NewWindow
if __name__ == "__main__":
    app = QApplication(argv)
    sg = NewWindow()
    sg.show()
    exit(app.exec())