from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=uic.loadUi('resources/login.ui', self)
        self.show()
        self.setStyleSheet("""
                    QMainWindow {
                        background-image: url(C:/workspace/개인공부/pygame/pythonProject/resources/images/로그인.png);
                    }
                """)
