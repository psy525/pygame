from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from crud.login.login_mapper import *
from crud.account.account_mapper import *


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
        self.loginButton.clicked.connect(self.login)
        self.loginMapper= LoginMapper()
        self.accountMapper= AccountMapper()
        self.state=0 #로그인 상태 초기화(0: 로그아웃, 1:로그인)
        self.show()

    def login(self):
        userId = self.idLine.text()
        password = self.pwLine.text()

        if not self.accountMapper.exist_user_check(userId):
            QMessageBox.warning(self, "로그인 실패", "존재하지 않는 아이디입니다.")
            return

        user = self.loginMapper.selectUser(userId)
        if user is None or user['password'] != password:
            QMessageBox.warning(self, "로그인 실패", "비밀번호가 틀렸습니다.")
        else:
            self.state = 1  # 로그인 성공
            QMessageBox.information(self, "로그인 성공", "로그인 성공")
            self.close()
            # 해야할 것
            # self.open_board()  # 로그인 성공 시 게시판 열기

    # def open_board(self):
    #     if self.state == 1:
    #         # 게시판을 여는 코드
    #         self.boardWindow = BoardWindow()
    #         self.boardWindow.show()
    #     else:
    #         QMessageBox.warning(self, "접근 거부", "로그인 후 게시판에 접근할 수 있습니다.")