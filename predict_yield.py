import joblib
import numpy as np

# Load trained model
model = joblib.load("ml_models/yield_model.pkl")


def predict_yield(rainfall, temperature, fertilizer):
    data = np.array([[rainfall, temperature, fertilizer]])

    prediction = model.predict(data)

    return float(prediction[0])