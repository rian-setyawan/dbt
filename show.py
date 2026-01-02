# import sys
# from pathlib import Path

# model = sys.argv[1]
# sql_path = Path("dbt_ci/models") / f"{model}.sql"

# if not sql_path.exists():
#     raise FileNotFoundError(sql_path)

# sql = sql_path.read_text()

# if "select" not in sql.lower():
#     raise ValueError("Invalid SQL")

# print("✅ SQL validation passed")

import sys
from pathlib import Path

if len(sys.argv) < 2:
    raise ValueError("Ticket ID harus diisi, contoh: python show.py EDM-0001")

ticket_id = sys.argv[1]
ticket_path = Path("dbt_ci/models") / ticket_id
print(ticket_path)
if not ticket_path.exists():
    raise FileNotFoundError(f"Ticket {ticket_id} tidak ditemukan")

print(f"Validasi ticket: {ticket_id}")

for sql_file in ticket_path.rglob("*.sql"):
    print(f"Checking SQL: {sql_file}")
