import os
import sys

MODEL = sys.argv[1] if len(sys.argv) > 1 else None

if not MODEL:
    print("❌ Model name required")
    sys.exit(1)

# compiled_path = f"dbt_project/target/compiled/dbt_ci/models/{MODEL}.sql"
compiled_path = f"dbt_ci/target/compiled/dbt_ci/models/{MODEL}.sql"

if not os.path.exists(compiled_path):
    print("❌ Compiled SQL not found:", compiled_path)
    sys.exit(1)

with open(compiled_path) as f:
    sql = f.read().lower()

print("===== COMPILED SQL =====")
print(sql)

# contoh rule CI
if "select *" in sql:
    print("❌ select * is not allowed")
    sys.exit(1)

if "join" in sql and "on" not in sql and "using" not in sql:
    print("❌ join without condition")
    sys.exit(1)

print("✅ SQL validation passed")
