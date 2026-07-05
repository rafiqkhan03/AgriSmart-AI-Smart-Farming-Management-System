from database.database import get_connection
import mysql.connector


# Add Farm
def create_farm(user_id, farm_name, location, soil_type, farm_size, crop_type):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO farms (user_id, farm_name, location, soil_type, farm_size, crop_type)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (user_id, farm_name, location, soil_type, farm_size, crop_type)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return {"message": "Farm created successfully"}

    except mysql.connector.Error as err:
        return {"error": str(err)}


# Get All Farms
def get_farms():
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM farms"

        cursor.execute(query)
        farms = cursor.fetchall()

        cursor.close()
        connection.close()

        return farms

    except mysql.connector.Error as err:
        return {"error": str(err)}