import mysql.connector

def stream_user_ages():
    """Generator that yields user ages one by one from the database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Server@2025',
            database='ALX_prodev'
        )
        cursor = connection.cursor()

        cursor.execute("SELECT age FROM user_data")
        
        for (age,) in cursor:
            yield age

    except mysql.connector.Error as err:
        print(f"Database error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def calculate_average_age():
    """Calculate average age using the generator without loading all data into memory."""
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        print("No users found.")
        return

    average = total_age / count
    print(f"Average age of users: {average:.2f}")

if __name__ == "__main__":
    calculate_average_age()
