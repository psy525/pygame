from PyQt5.QtWidgets import *
from PyQt5 import uic
from crud.account.account_service import *
class SignWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=uic.loadUi('resources/sign.ui', self)
        self.setStyleSheet("""
                    QMainWindow {
                        background-image: url(C:/workspace/개인공부/pygame/pythonProject/resources/images/회원가입.png);
                    }
                """)
        # self.idcheckBtn.clicked.connect(self.idCheck)
        # self.phcheckBtn.clicked.connect(self.phCheck)
        self.registButton.clicked.connect(self.register)
        self.accountService=AccountService()
        self.show()


    def register(self):
        print("회원가입 버튼 클릭")
        userId=self.idLine.text()
        password=self.pwLine.text()
        userName=self.nameLine.text()
        ph=self.phLine.text()
        result=self.accountService.registerAccount(userId,password,userName,ph)
        print("result확인용 %s" %result)
        if result:
            QMessageBox.information(self, "확인", "회원가입 완료")
        else:
            QMessageBox.information(self, "확인", "회원가입 실패")
        self.close()
