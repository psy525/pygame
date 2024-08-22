from PyQt5.QtWidgets import *
from PyQt5 import uic
from crud.account.account_service import *
from crud.account.account_mapper import *
class SignWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=uic.loadUi('resources/sign.ui', self)
        self.setStyleSheet("""
                    QMainWindow {
                        background-image: url(C:/workspace/개인공부/pygame/pythonProject/resources/images/회원가입.png);
                    }
                """)
        self.idcheckBtn.clicked.connect(self.idCheck)
        self.phcheckBtn.clicked.connect(self.phCheck)
        self.registButton.clicked.connect(self.register)
        self.accountService=AccountService()
        self.accountMapper=AccountMapper()
        self.id_check=False
        self.ph_check=False
        self.show()


    def register(self):
        print("회원가입 버튼 클릭")
        if not self.id_check:
            QMessageBox.warning(self, "경고", "아이디 중복 체크를 완료하세요.")
            return
        if not self.ph_check:
            QMessageBox.warning(self, "경고", "전화번호 중복 체크를 완료하세요.")
            return
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

    def idCheck(self):
        id=self.idLine.text()
        if self.accountMapper.exist_user_check(id):
            QMessageBox.warning(self, "확인", "이미 존재하는 아이디입니다.")
        else:
            QMessageBox.information(self, "확인", "사용 가능한 아이디입니다.")
            self.id_check = True

    def phCheck(self):
        ph=self.phLine.text()
        if self.accountMapper.exist_ph_check(ph):
            QMessageBox.warning(self, "확인", "이미 존재하는 번호입니다.")
        else:
            QMessageBox.information(self, "확인", "사용 가능한 번호입니다.")
            self.ph_check=True