import sqlite3

class DBconnection:
    def __init__(self):
        self.db = 'database/dbhistory.db'
        self.connection = sqlite3.connect(self.db)
        self.cur = self.connection.cursor()

    def close_connection(self):
        self.connection.commit()
        self.connection.close()


