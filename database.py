print("✅ LOADED database.py FROM:", __file__)

import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self,
                 host="mysql-berke.alwaysdata.net",
                 user="berke_jetski",
                 password="Jetski1234@",
                 database="berke_jetski",
                 port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None

    def connect(self):
        print("➡️ Trying with user:", self.user)
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            if self.connection.is_connected():
                print("✅ Connected to berke_jetski database")
                return True
        except Error as e:
            print("❌ Error while connecting to MySQL:", e)
        return False

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("🔌 Database connection closed")

    def fetch_all(self, query, params=None):
        if not self.connection or not self.connection.is_connected():
            ok = self.connect()
            if not ok:
                return []

        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        rows = cursor.fetchall()
        cursor.close()
        return rows
