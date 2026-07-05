import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv("ml_models/crop_data.csv")

# Features (inputs)
X = data[["rainfall", "temperature", "fertilizer"]]

# Target (output)
y = data["yield"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "ml_models/yield_model.pkl")

print("Model trained and saved successfully")