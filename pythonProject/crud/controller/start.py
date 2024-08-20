from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from game.test게임 import *
from crud.login.login import *
from resources import *
class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=uic.loadUi('resources/gameWindow.ui', self)
        self.startButton.clicked.connect(self.start_game)
        self.loginButton.clicked.connect(self.login)


    def start_game(self):
        self.close()  # 현재 메인 메뉴를 닫고
        print("start_game")
        start_game()

    def login(self):
        self.login=LoginWindow()