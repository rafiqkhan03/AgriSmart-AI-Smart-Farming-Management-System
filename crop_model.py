from database.database import get_connection
import mysql.connector


# Add Crop
def create_crop(farm_id, crop_name, planting_date, expected_harvest):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO crops (farm_id, crop_name, planting_date, expected_harvest)
            VALUES (%s, %s, %s, %s)
        """

        values = (farm_id, crop_name, planting_date, expected_harvest)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return {"message": "Crop added successfully"}

    except mysql.connector.Error as err:
        return {"error": str(err)}


# Get All Crops
def get_crops():
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM crops"

        cursor.execute(query)
        crops = cursor.fetchall()

        cursor.close()
        connection.close()

        return crops

    except mysql.connector.Error as err:
        return {"error": str(err)}