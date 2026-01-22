import mysql.connector 
from mysql.connector.connection import MySQLConnectionAbstract 
import os


MYSQL_ROOT_USER = os.getenv("MYSQL_ROOT_USER")
MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_ROOT_HOST = os.getenv("MYSQL_ROOT_HOST")
MYSQL_ROOT_DB = os.getenv("MYSQL_ROOT_DB")



def get_connection():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="mydatabase")
    return mydb

def creat_table(mydb:MySQLConnectionAbstract):
    mycursor = mydb.cursor()
    mycursor.execute("""
    CREATE TABLE IF NOT EXIST weapons_list (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    weapon_id VARCHAR(250), 
                    weapon_name VARCHAR(250),
                    weapon_type VARCHAR(250), 
                    range_km INT,
                    weight_kg FLOAT,
                    manufacturer VARCHAR(250), 
                    origin_country VARCHAR(250), 
                    storage_location VARCHAR(250) ,
                    year_estimated INT, 
                    level_risk VARCHAR(250))""")
    