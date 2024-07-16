import mysql.connector
from mysql.connector import Error

host = "localhost"
user = "melvin_032"
password = "Immelvin_032mysql"
schema = "batman"
database = "crud"
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_data(connection, data):
    cursor = connection.cursor()
    try:
        for item in data:
            cursor.execute(f"INSERT INTO {schema}.{database} (id, studname, contact, department) VALUES (%s, %s, %s, %s)", item)
        connection.commit()
        print("Data inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# Connection details
connection = create_connection("localhost", "melvin_032", "Immelvin_032mysql", "batman")

# Data to insert
data_to_insert = [
    ("2022-MN-05161-0", "Melvin Sarabia", "09624764646", "ITECH"),
    ("2024-SM-67890-1", "Sophie Montemayor", "09876543210", "COC"),
    ("2025-PP-54321-2", "Patricia Pascual", "09765432109", "CAF"),
    ("2023-CS-09876-3", "Casey Dolovin", "09111222334", "CCIS"),
    ("2024-SB-56789-4", "Sarah Brown", "09223334445", "CEA"),
    ("2025-CW-23456-5", "Chris Wilson", "09334445556", "CBA"),
    ("2023-AM-34567-6", "Anna Martinez", "09445556667", "CAL"),
    ("2024-JT-45678-7", "James Taylor", "09556667778", "COED"),
    ("2025-LL-87654-8", "Laura Lee", "09667778889", "CPSPA"),
    ("2023-RC-76543-9", "Robert Clark", "09778889990", "CL"),
    ("2023-MH-24680-0", "Michael Harris", "09123456780", "ITECH"),
    ("2024-JC-13579-1", "Jennifer Carter", "09876543201", "COC"),
    ("2025-AB-97531-2", "Adam Baker", "09765432102", "CAF"),
    ("2023-ER-75319-3", "Emma Roberts", "09111222303", "CCIS"),
    ("2024-SD-86420-4", "Steven Davis", "09223334404", "CEA"),
    ("2025-LB-13579-5", "Linda Brown", "09334445505", "CBA"),
    ("2023-AM-02468-6", "Andrew Miller", "09445556606", "CAL"),
    ("2024-JB-98765-7", "Jessica Bell", "09556667707", "COED"),
    ("2025-RL-13579-8", "Ryan Lewis", "09667778808", "CPSPA"),
    ("2023-RC-98765-9", "Rebecca Campbell", "09778889909", "CL")
]

# Insert data
insert_data(connection, data_to_insert)
