import mysql.connector

# DB_CONFIG = {
#     'user': 'root',
#     'password': 'Server@2025',
#     'host': 'localhost',
#     'database': 'ALX_prodev'
# }


def stream_users():
    '''To stream users from Mysql database one by one'''
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Server@2025', 
            database='ALX_prodev'
        )
        cursor = connection.cursor()

        '''Query execution'''
        cursor.execute("SELECT user_id, name, email, age FROM user_data")

        for user_id, name, email, age in cursor:
            yield f"User_Id: {user_id}, Name: '{name}', Email: '{email}', Age: {age}"
        
        for row in cursor:
            yield row
        print("Data retrieved!")

    except mysql.connector.Error as err:
        print(f"Data retrieval error: {err}")
    
    # finally:
    #     if cursor:
    #         cursor.close()
    #     if  connection:
    #         connection.close()
