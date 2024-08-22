import oracledb

class DBManager():
    def __init__(self, username, password, dsn):
        print("오라클 생성")
        self.username = username
        self.password = password
        self.dsn = dsn
        self.connection=None

    def connect(self):
        print("Connection 시도")
        try:
            self.connection = oracledb.connect(user=self.username, password=self.password, dsn=self.dsn)
            print("Connection successful")
        except oracledb.DatabaseError as err:
            print(err)

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")

    def sql_execute(self, sql, params):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, params or ())
            self.connection.commit()
            cursor.close()
            print("SQL command executed successfully")
        except oracledb.DatabaseError as err:
            print(f"SQL execute error: {err}")

    def sql_fetchone(self, sql, params):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params)
                return cursor.fetchone()
        except oracledb.Error as e:
            print(f"Error fetching SQL result: {e}")
            return None

    def fetch_data(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except oracledb.DatabaseError as err:
            print(err)
            return None

