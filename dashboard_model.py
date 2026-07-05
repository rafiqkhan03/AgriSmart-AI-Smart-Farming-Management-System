from database.database import get_connection
import mysql.connector


def get_dashboard_stats():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Count users
        cursor.execute("SELECT COUNT(*) FROM users")
        users = cursor.fetchone()[0]

        # Count farms
        cursor.execute("SELECT COUNT(*) FROM farms")
        farms = cursor.fetchone()[0]

        # Count crops
        cursor.execute("SELECT COUNT(*) FROM crops")
        crops = cursor.fetchone()[0]

        # Count predictions
        cursor.execute("SELECT COUNT(*) FROM predictions")
        predictions = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return {
            "total_users": users,
            "total_farms": farms,
            "total_crops": crops,
            "total_predictions": predictions
        }

    except mysql.connector.Error as err:
        return {"error": str(err)}
    

def get_yield_trend():
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT created_at, predicted_yield
            FROM predictions
            ORDER BY created_at
        """

        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return data

    except mysql.connector.Error as err:
        return {"error": str(err)}