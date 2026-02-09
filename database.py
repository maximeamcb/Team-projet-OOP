import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="mysql-berke.alwaysdata.net",
                user="berke",
                password="Jetski1234@",
                database="berke_jetski"
            )

            if self.connection.is_connected():
                print("✅ Connected to berke_jetski database")

        except Error as e:
            print("❌ Error while connecting to MySQL:", e)

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("🔌 Database connection closed")
