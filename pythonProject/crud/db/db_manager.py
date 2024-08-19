import oracledb

class DBManager():
    def __init__(self, username, password, dsn):
        self.username = username
        self.password = password
        self.dsn = dsn
        self.coonection=None

    def connect(self):
        try:
            self.connection=oracledb.connect(user=self.username, password=self.password, dsn=self.dsn)
            print("Connection successful")
        except oracledb.DatabaseError as err:
            print(err)

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")

    def fetch_data(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except oracledb.DatabaseError as err:
            print(err)
            return None