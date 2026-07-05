from fastapi import UploadFile
import shutil
import os

from database.database import get_connection
from ml_models.detect_disease import predict_disease


def save_prediction(image_name, disease, confidence):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO disease_predictions
        (image_name, disease, confidence)
        VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (image_name, disease, confidence)
    )

    connection.commit()

    cursor.close()
    connection.close()


def detect_disease(file: UploadFile):

    # Make sure uploads folder exists
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    # Predict disease
    result = predict_disease(file_path)

    # Save prediction to database
    save_prediction(
        file.filename,
        result["disease"],
        result["confidence"]
    )

    return result

def get_all_predictions():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT *
        FROM disease_predictions
        ORDER BY created_at DESC
    """

    cursor.execute(query)

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records
import pandas as pd
from fastapi.responses import FileResponse


def export_predictions():

    connection = get_connection()

    query = """
        SELECT *
        FROM disease_predictions
        ORDER BY created_at DESC
    """

    df = pd.read_sql(
        query,
        connection
    )

    connection.close()

    file_path = "prediction_report.csv"

    df.to_csv(
        file_path,
        index=False
    )

    return file_path