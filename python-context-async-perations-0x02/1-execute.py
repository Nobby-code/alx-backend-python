import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params or ()
        self.conn = None
        self.cursor = None
        self.results = None
    
    def __enter__(self):
        print("Opening database connection..")
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        #Executing query with params
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type:
            print(f"An error occurred: {exc_value}")
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()
        print("Database connection closed.")

query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery('users.db', query, params) as results:
    print("Query Results (age > 25):")
    for row in results:
        print(row)