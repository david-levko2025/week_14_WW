from pandas import DataFrame
import mysql.connector 
import os


def get_connection():
    my_connection = mysql.connector.connect(
    host=os.getenv("MYSQL_ROOT_HOST") ,
    user=os.getenv("MYSQL_ROOT_USER"),
    password=os.getenv("MYSQL_ROOT_PASSWORD"),
    database=os.getenv("MYSQL_ROOT_DB"))
    return my_connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = """
            CREATE TABLE IF NOT EXISTS weapons_list
            (id INT AUTO_INCREMENT PRIMARY KEY,
            weapon_id VARCHAR(250),
            weapon_name VARCHAR(250),
            weapon_type VARCHAR(250),
            range_km INT,
            weight_kg FLOAT,
            manufacturer VARCHAR(250),
            origin_country VARCHAR(250),
            storage_location VARCHAR(250),
            year_estimated INT,
            risk_level VARCHAR(250))
        """
    cursor.execute(sql)

def insert_data_to_db(df:DataFrame):
    connection = get_connection()
    cursor = connection.cursor()
    sql = """
    INSERT INTO weapons (
    weapon_id,
    weapon_name,
    weapon_type,
    range_km,
    weight_kg,
    manufacturer,
    origin_country,
    storage_location,
    year_estimated,
    risk_level ) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """