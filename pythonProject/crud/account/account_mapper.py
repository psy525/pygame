from crud.db.db_manager import DBManager

class AccountMapper:
    db=None

    def __init__(self):
        print("회원가입 mapper")
        self.db = DBManager("std205", "oracle21c", "nextit.or.kr:1521/xe")
        self.db.connect()
    def insertContent(self, accountVo):
        print("회원가입 정보 넣기")
        sql = "INSERT INTO GAME_USERS(user_id, password, user_name, phnumber) VALUES (:1, :2, :3, :4)"
        params = (accountVo.userId, accountVo.password, accountVo.userName, accountVo.ph)
        self.db.sql_execute(sql, params)

    def exist_user_check(self, userId):
        sql = "SELECT COUNT(1) FROM GAME_USERS WHERE user_id = :1"
        params = (userId,)
        result = self.db.sql_fetchone(sql, params)
        if result:
            return result[0] > 0
        return False

    def exist_ph_check(self, ph):
        sql = "SELECT COUNT(1) FROM GAME_USERS WHERE PHNUMBER = :1"
        params = (ph,)
        result = self.db.sql_fetchone(sql, params)
        if result:
            return result[0] > 0
        return False