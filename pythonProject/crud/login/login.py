from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=uic.loadUi('resources/login.ui', self)
        self.show()
