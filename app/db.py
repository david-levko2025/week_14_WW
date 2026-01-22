import mysql.connector 


class DBConnection:

    @staticmethod
    def create_connection():
        config = {'user': 'user',
                    'password': '12345678',
                    'host': '127.0.0.1',
                    'database': 'weapon_warehouse',
                    'raise_on_warnings': True}
        connection = mysql.connector.connect(**config)
        return connection

    @staticmethod
    def create_db():
        conn = DBConnection.create_connection()
        cursor = conn.cursor()
        query = "CREATE DB IF NOT EXISTS weapon_warehouse"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        return "dataBase created"


    @staticmethod
    def create_table():
        conn = DBConnection.create_connection()
        cursor = conn.cursor()
        query = """ CREATE TABLE IF NOT EXISTS 'weapons_list' (
                            `ID` INT PRIMARY_KEY AUTO_INCREMENT,
                            `weapon_id` VARCHAR(250),
                            `weapon_name` VARCHAR(250),
                            `weapon_type` VARCHAR(250),
                            `range_km` INT,
                            `weight_kg` FLOAT,
                            `manufacturer` VARCHAR(250),
                            `origin_country` VARCHAR(250),
                            `storage_location` VARCHAR(250),
                            `year_estimated` INT,
                            `risk_level` VARCHAR(250))"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        return "table created"


    @staticmethod
    def insert_data(clean_db):
        conn = DBConnection.create_connection()
        cursor = conn.cursor()
        query = """INSERT INTO weapons_list(weapon_name, weapon_type, range_km, weight_kg, manufacturer,
                        origin_country, storage_location, year_estimated, risk_level)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        for row in clean_db:
            cursor.execute(query, (row["weapon_name"],
                                    row["weapon_type"],
                                    row["range_km"],
                                    row["weight_kg"],
                                    row["manufacturer"],
                                    row["origin_country"],
                                    row["storage_location"],
                                    row["year_estimated"],
                                    row["risk_level"],),)
        conn.commit()
        cursor.close()
        return "succesfully inserted"