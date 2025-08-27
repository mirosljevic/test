from database import PostgresClient
from pathlib import Path


def sql_file_execution():
    sql_file = Path("sample_query.sql")

    with sql_file.open("w") as f:
        f.write("SELECT * FROM users WHERE active = %s")

    with PostgresClient(host="localhost", port=5432, database="test_db",
                        username="test_user", password="test_pass") as db:
        results = db.execute_query_from_file(sql_file, params=(True,), fetch=True)
        print(f"Results from SQL file: {len(results)} rows")

        for row in results:
            print(f"User: {row['name']}")

    sql_file.unlink()


if __name__ == "__main__":
    sql_file_execution()
