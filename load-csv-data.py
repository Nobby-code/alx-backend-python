import requests
import csv
import uuid
import os

# url = 'https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2024/12/3888260f107e3701e3cd81af49ef997cf70b6395.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20250517%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250517T165407Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ed02ab2bf33f4dd792f4688fd4df57eb076954417a24c1dd8825a5d18ff98f02'

# response = requests.get(url)
# if response.status_code == 200:
#     with open('user_data.csv', 'wb') as file:
#         file.write(response.content)
#     print("File saved as user_data.csv")
# else:
#     print(f"Failed to download data, Erroro code: {response.status_code}")


def load_csv_data(url):
    """Reads CSV and returns list of tuples for insertion."""
    user_records = []
    try:
        # Get the full path to the file in the current working directory
        file_path = os.path.join(os.getcwd(), url)
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{url} not found in {os.getcwd()}")
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