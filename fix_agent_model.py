import sqlite3
import json

db = sqlite3.connect(r"C:\Users\Deep.LAPTOP-ID5I37OE\.openjarvis\agents.db")
cur = db.cursor()

rows = cur.execute(
    "SELECT id, config_json FROM managed_agents"
).fetchall()

for agent_id, cfg in rows:
    data = json.loads(cfg or "{}")
    data["model"] = "qwen3:8b"

    cur.execute(
        "UPDATE managed_agents SET config_json=? WHERE id=?",
        (json.dumps(data), agent_id),
    )

db.commit()
db.close()

print("✅ All agents updated to qwen3:8b")