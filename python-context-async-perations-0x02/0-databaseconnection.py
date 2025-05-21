import sqlite3

class DatabaseConnection():
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        print('Creating db connection..')
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(f"An exception occurred: {exc_value}")
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()
        print("Database connection closed.")
    
with DatabaseConnection('users.db') as cursor:
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL)
                ''')
    cursor.executemany("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                    [
                        ("Norbert", "norbert@example.com", 28),
                        ("Gevil", "gevil@example.com", 22)
                    ])
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    print("Registered users:")
    print(results)