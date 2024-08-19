
class AccountService:
    accountMapper=None
    def __init__(self):
        self.accountMapper=AccountMapper()
