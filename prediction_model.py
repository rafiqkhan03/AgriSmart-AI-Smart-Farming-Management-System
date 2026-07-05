from database.database import get_connection
from ml_models.predict_yield import predict_yield
import mysql.connector


def create_prediction(crop_id, rainfall, temperature, fertilizer):
    try:
        # Get prediction from model
        predicted = predict_yield(
            rainfall,
            temperature,
            fertilizer
        )

        # Save to database
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO predictions (
                crop_id,
                rainfall,
                temperature,
                fertilizer,
                predicted_yield
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            crop_id,
            rainfall,
            temperature,
            fertilizer,
            predicted
        )

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return {
    "predicted_yield": round(predicted, 2)
}

    except mysql.connector.Error as err:
        return {"error": str(err)}