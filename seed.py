import csv
import uuid
import mysql.connector
from mysql.connector import errorcode

DB_CONFIG = {
    'user': 'root',
    'password': 'Server@2025',
    'host': 'localhost'
}

DATABASE_NAME = 'ALX_prodev'

def connect_db():
    '''Connect to MySQL Server'''
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("MySQL Server Created")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    '''Create ALX_Prodev database if it doesnot exist'''
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}")
        print(f"Database {DATABASE_NAME} created!")
    except mysql.connector.Error as err:
        print(f"Failed to create database {err}")

def connect_to_prodev():
    '''Connect to ALX_prodev database'''
    config = DB_CONFIG.copy()
    config['database'] = DATABASE_NAME
    try:
        connection = mysql.connector.connect(**config)
        print(f"Connected successfully to {DATABASE_NAME}")
        return connection
    except mysql.connector.Error as err:
        print(f"Error {err}")
        return None
    
def create_table(connection):
    '''Create table if it doesnot exist'''
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL(3,0) NOT NULL,
        INDEX (user_id)
    )
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        print("table created")

    except mysql.connector.Error as err:
        print(f"Error while creating table: {err}")

def insert_data(connection, data):
    """Inserts data into user_data table, ignoring duplicates."""
    insert_sql = """
    INSERT INTO user_data (user_id, name, email, age)
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE user_id = user_id
    """
    try:
        if isinstance(data, str):  # If passed a file path instead of list of tuples
            print(f"🔁 Loading data from file: {data}")
            data = load_csv_data(data)  # Call the existing CSV loader

        if not isinstance(data, list) or not all(isinstance(row, tuple) for row in data):
            raise ValueError("Data must be a list of tuples or a CSV file path")
        cursor = connection.cursor()
        for row in data:
            cursor.executemany(insert_sql, data)
        connection.commit()
        print(f"Inserted {cursor.rowcount} records")
    except mysql.connector.Error as err:
        print(f"Eror while inserting data: {err}")


def load_csv_data(url):
    """Reads CSV and returns list of tuples for insertion."""
    user_records = []
    try:
        with open(url, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name'].strip()
                email = row['email'].strip()
                age = int(row['age'])
                user_records.append((user_id, name, email, age))
            print(f"Loaded {len(user_records)} users from CSV.")
            return user_records
    except Exception as err:
        print(f"Error reading CSV: {err}")
        return []


    
