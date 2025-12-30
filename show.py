import sys
from pathlib import Path

model = sys.argv[1]
sql_path = Path("dbt_ci/models") / f"{model}.sql"

if not sql_path.exists():
    raise FileNotFoundError(sql_path)

sql = sql_path.read_text()

if "select" not in sql.lower():
    raise ValueError("Invalid SQL")

print("✅ SQL validation passed")