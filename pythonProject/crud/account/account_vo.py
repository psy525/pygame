from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class AccountWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=uic.loadUi('../resources/account.ui', self)
        print("회원가입 창 생성")
        self.idcheckBtn.clicked.connect(self.checkId)
        self.phcheckBtn.clicked.connect(self.checkPh)
        self.registButton.clicked.connect(self.register)
        self.accountService=AccountService()

