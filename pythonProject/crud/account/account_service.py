from crud.account.account_mapper import AccountMapper
from crud.account.account_mapper import *
from crud.account.account_vo import *

class AccountService:
    accountMapper=None

    def __init__(self):
        print("회원가입 서비스")
        self.accountMapper = AccountMapper()

    def registerAccount(self, userId, password, userName, ph):
        print("회원가입: 작성")

        accountVo=AccountVo()
        accountVo.userId=userId
        accountVo.password=password
        accountVo.userName=userName
        accountVo.ph=ph

        try:
            self.accountMapper.insertContent(accountVo)
            return True # 회원가입 완료시 알림창 띄게하기 위함
        except Exception as e:
            print("회원가입 중 에러 발생")
            return False
