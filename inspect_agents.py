import sqlite3

db = sqlite3.connect(r"C:\Users\Deep.LAPTOP-ID5I37OE\.openjarvis\agents.db")
cur = db.cursor()

print("=== TABLES ===")
tables = cur.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
).fetchall()

for table in tables:
    print(table[0])

print("\n=== managed_agents Schema ===")
for row in cur.execute("PRAGMA table_info(managed_agents)"):
    print(row)

print("\n=== managed_agents Data ===")
rows = cur.execute("SELECT * FROM managed_agents").fetchall()
for row in rows:
    print(row)