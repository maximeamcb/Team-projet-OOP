from database import Database

db = Database()
db.connect()
print(db.fetch_all("SHOW TABLES;"))
db.disconnect()
