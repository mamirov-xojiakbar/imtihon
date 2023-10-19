from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QLineEdit, QLabel, QPushButton
from PyQt6.QtWidgets import QRadioButton, QWidget
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtCore import QRect

class SignInWindow(QWidget):

    def __init__(self, w=500, h=500) -> None:
        super().__init__()
        self.my_width = w
        self.my_height = h
        self.setUi()

    def setUi(self):
        w = QApplication.primaryScreen().size().width()
        h = QApplication.primaryScreen().size().height()
        self.setGeometry(w//2 - self.my_width // 2,
                         h//2 - self.my_height // 2,
                         self.my_width, self.my_height)
        
        #Logo
        self.logoLbl = QLabel(self)
        self.logoLbl.setPixmap(QPixmap("icons/diagram.png"))
        self.logoLbl.setGeometry(self.my_width//2-50, 10, 150, 150)
        self.logoLbl.setScaledContents(True)

        #Emailni kiritish maydoni
        self.emailEdit = QLineEdit(self)
        self.emailEdit.setGeometry(self.my_width//2-100, 180, 250, 40)
        self.my_font = QFont("Times New Roman", 14, 4)
        self.emailEdit.setFont(self.my_font)
        self.emailEdit.setPlaceholderText("example@gmail.com")

        #Parolni kiritish maydoni
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setGeometry(self.my_width//2-100, 235, 250, 40)
        self.my_font = QFont("Times New Roman", 14, 4)
        self.passwordEdit.setFont(self.my_font)
        self.emailEdit.setPlaceholderText("Parolni kiriting")
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

        #Remember me
        self.remem = QRadioButton(self)
        self.remem.setText("Remember me")
        self.remem.setGeometry(self.my_width//2-50, 285, 200, 25)
        self.remem.setFont(self.my_font)

        #Buttonlar
        self.sgnInBtn = QPushButton("Sign In", self)
        self.sgnInBtn.setGeometry(50,335,180,45)
        self.sgnUpBtn = QPushButton("Sign Up", self)
        self.sgnUpBtn.setGeometry(270, 335, 180, 45)