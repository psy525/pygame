from crud.db.db_manager import DBManager

class LoginMapper:
    db=None

    def __init__(self):
        print("회원가입 mapper")
        self.db = DBManager("std205", "oracle21c", "nextit.or.kr:1521/xe")
        self.db.connect()
    def selectUser(self, userId):
        print("로그인 유저 확인")
        sql = "SELECT user_id, password FROM GAME_USERS where user_id = :1"
        params = (userId,)
        result=self.db.sql_fetchone(sql, params)
        if result:
            return {'userId': result[0], 'password': result[1]}
        return None
