from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from game.test게임 import *
from crud.login.login import *
from resources import *
from crud.account.account import *


class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('resources/gameWindow.ui', self)

        font_id_omu = QFontDatabase.addApplicationFont("game/omyu_pretty.ttf")
        if font_id_omu != -1:  # 폰트 로드 성공 시
            omyu_family = QFontDatabase.applicationFontFamilies(font_id_omu)[0]

        # 두 번째 폰트 로드
        font_id_jalan = QFontDatabase.addApplicationFont("game/Jalnan2.otf")
        if font_id_jalan != -1:  # 폰트 로드 성공 시
            jalan_family = QFontDatabase.applicationFontFamilies(font_id_jalan)[0]


        self.setStyleSheet("""
                                QMainWindow {{
                background-image: url(E:/sql/git/pygame/pythonProject/resources/images/sky.png);
            }}
            QLabel#label_omu {{
                font-family: '{omu_family}';
                font-size: 14pt;
            }}
            QPushButton#button_jalan {{
                font-family: '{jalan_family}';
                font-size: 10pt;
            }}
                            """)
        self.startButton.clicked.connect(self.start_game)
        self.loginButton.clicked.connect(self.login)
        self.signupButton.clicked.connect(self.signup)


    def start_game(self):
        self.close()  # 현재 메인 메뉴를 닫고
        print("start_game")
        start_game()
        score_window = ScoreWindow(100)
        score_window.exec()

    def login(self):
        self.login = LoginWindow()

    def signup(self):
        self.signup = SignWindow()
