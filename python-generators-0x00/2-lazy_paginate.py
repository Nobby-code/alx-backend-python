import mysql.connector

def paginate_users(page_size, offset):
    """Fetch a page of users from the database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Server@2025',
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        rows = cursor.fetchall()

        return rows

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return []

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def lazy_paginate(page_size):
    """Generator to lazily fetch paginated data one page at a time."""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page  # Yield one page (list of user dicts)
        offset += page_size  # Update offset for the next page
