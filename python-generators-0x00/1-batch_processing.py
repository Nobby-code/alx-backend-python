import mysql.connector

def stream_users_in_batches(batch_size):
    '''Generator that yields users from database in batches'''

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Server@2025', 
            database='ALX_prodev'
        )

        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def batch_processing(batch_size):
    """
    Processes each batch and yields users over age 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                yield user

if __name__ == '__main__':
    for user in batch_processing(5):  # or whatever batch size you want
        print(f"User_Id: {user['user_id']}, Name: {user['name']}, Age: {user['age']}")