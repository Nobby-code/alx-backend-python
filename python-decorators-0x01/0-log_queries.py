import sqlite3
import functools
from datetime import datetime

#### decorator to lof SQL queries

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query_info = f"Execution start: [{datetime.now()}] Executing function: {func.__name__}"
        print(query_info)

        '''Create Users table'''
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()


        create_table = '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL)
                '''
        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute(create_table)
            cursor.execute("SELECT COUNT(*) FROM users")
            if cursor.fetchone()[0] == 0:
                cursor.executemany(
                    "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                    [
                        ("Norbert", "norbert@example.com", 29),
                        ("Gevil", "gevil@example.com", 22)
                    ]
                )
            conn.commit()

        query_result = func(*args, **kwargs)
        print(f"Execution end: [{datetime.now()}] Executing function: {func.__name__}\n")
        return query_result
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
print("Users in the database")
for user in users:
    print(user)