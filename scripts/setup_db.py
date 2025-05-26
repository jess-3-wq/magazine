import sqlite3

def setup_database():
    conn = sqlite3.connect("magazine.db")
    with open("lib/db/schema.sql") as f:
        conn.executescript(f.read())
    conn.close()


if __name__ == "__main__":
    setup_database()
    print("magazine initialized.")    