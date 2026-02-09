import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(
        self,
        host="mysql-berke.alwaysdata.net",
        user="berke",
        password="Jetski1234@",
        database="berke_jetski",
        port=3306,
    ):
        selfself = self  # (ignore if your editor highlights; harmless)
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

        self.connection = None

    def connect(self):
        """Open the MySQL connection."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                autocommit=False,
            )

            if self.connection.is_connected():
                print("✅ Connected to MySQL database")

        except Error as e:
            print("❌ Error while connecting to MySQL:", e)
            self.connection = None

    def disconnect(self):
        """Close the MySQL connection."""
        try:
            if self.connection and self.connection.is_connected():
                self.connection.close()
                print("🔌 Database connection closed")
        except Error as e:
            print("❌ Error while closing connection:", e)

    def _ensure_connected(self):
        """Reconnect automatically if needed."""
        if not self.connection or not self.connection.is_connected():
            self.connect()

    def fetch_all(self, query, params=None):
        """Run a SELECT and return all rows (list of dicts)."""
        self._ensure_connected()
        if not self.connection:
            return []

        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except Error as e:
            print("❌ Error while fetching data:", e)
            return []

    def fetch_one(self, query, params=None):
        """Run a SELECT and return one row (dict) or None."""
        self._ensure_connected()
        if not self.connection:
            return None

        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            row = cursor.fetchone()
            cursor.close()
            return row
        except Error as e:
            print("❌ Error while fetching one row:", e)
            return None

    def execute(self, query, params=None):
        """
        Run INSERT/UPDATE/DELETE.
        Returns number of affected rows.
        """
        self._ensure_connected()
        if not self.connection:
            return 0

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            self.connection.commit()
            affected = cursor.rowcount
            cursor.close()
            return affected
        except Error as e:
            print("❌ Error while executing query:", e)
            try:
                self.connection.rollback()
            except Exception:
                pass
            return 0
