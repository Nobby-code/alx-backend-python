import time
import sqlite3 
import functools

#### paste your with_db_decorator here

def with_db_connection(func):
    """ Handling of opening and closing of SQLite db""" 
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def retry_on_failure(retries=3, delay=2):
    '''Retry to reconnect when there is a failure'''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    attempt += 1
                    print(f"Attempt {attempt} failed: {err}")
                    if attempt < retries:
                        print(f"Retrying in {delay} second(s)...")
                        time.sleep(delay)
                    else:
                        print("All retries failed.")
                        raise
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)