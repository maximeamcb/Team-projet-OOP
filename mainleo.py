from database import Database

print("🚀 Test started")

db = Database()
db.connect()

tables = db.fetch_all("SHOW TABLES;")
print("📋 Tables in database:", tables)

db.disconnect()

print("✅ Test finished")
