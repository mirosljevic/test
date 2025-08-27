from database import PostgresClient


def basic_database_operations():
    with PostgresClient(host="localhost", port=5432, database="test_db",
                        username="test_user", password="test_pass") as db:

        users_data = [
            {"name": "John Doe", "email": "john@example.com"},
            {"name": "Jane Smith", "email": "jane@example.com"},
        ]

        for user in users_data:
            db.insert("users", user)

        all_users = db.select("users")
        print(f"Found {len(all_users)} users")

        specific_user = db.select("users", where="email = %s", params=("john@example.com",))
        print(f"User found: {specific_user}")

        db.update("users", {"name": "John Updated"}, where="email = %s", where_params=("john@example.com",))

        db.delete("users", where="email = %s", params=("jane@example.com",))


if __name__ == "__main__":
    basic_database_operations()
