from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from backend.user_model import create_user, login_user
from backend.farm_model import create_farm, get_farms
from backend.crop_model import create_crop, get_crops
from backend.prediction_model import create_prediction
from backend.dashboard_model import get_dashboard_stats
from backend.dashboard_model import get_yield_trend
from backend.disease_model import detect_disease
from fastapi import UploadFile, File
from backend.disease_model import get_all_predictions
from backend.disease_model import export_predictions
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from backend.weather_model import get_weather
from backend.irrigation_model import get_irrigation_recommendation
from backend.fertilizer_model import get_fertilizer_recommendation
from backend.price_model import predict_market_price
from backend.recommendation_logic import predict_crop, predict_fertilizer



app = FastAPI()

app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Smart Farming API running"}


@app.post("/register")
def register_user(name: str, email: str, password: str):
    return create_user(name, email, password)


@app.post("/login")
def login(email: str, password: str):
    return login_user(email, password)

@app.get("/admin/users")
def admin_list_users():
    try:
        from database.database import get_connection
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT id, name, email, created_at FROM users ORDER BY id DESC")
        users = cur.fetchall()
        cur.close()
        conn.close()
        return users
    except Exception as e:
        return {"error": str(e)}

@app.post("/add-farm")
def add_farm(user_id: int, farm_name: str, location: str, soil_type: str, farm_size: float, crop_type: str):
    return create_farm(user_id, farm_name, location, soil_type, farm_size, crop_type)


@app.get("/farms")
def list_farms():
    return get_farms()

@app.post("/add-crop")
def add_crop(
    farm_id: int,
    crop_name: str,
    planting_date: str,
    expected_harvest: str
):
    return create_crop(
        farm_id,
        crop_name,
        planting_date,
        expected_harvest
    )


@app.get("/crops")
def list_crops():
    return get_crops()

@app.post("/predict-yield")
def predict(
    crop_id: int,
    rainfall: float,
    temperature: float,
    fertilizer: float
):
    return create_prediction(
        crop_id,
        rainfall,
        temperature,
        fertilizer
    )

@app.get("/dashboard-stats")
def dashboard():
    return get_dashboard_stats()


@app.get("/yield-trend")
def yield_trend():
    return get_yield_trend()


@app.post("/detect-disease")
def disease(
    file: UploadFile = File(...)
):
    return detect_disease(file)


@app.get("/prediction-history")
def prediction_history():
    return get_all_predictions()

@app.get("/export-report")
def download_report():

    file_path = export_predictions()

    return FileResponse(
        path=file_path,
        filename="prediction_report.csv",
        media_type="text/csv"
    )

@app.get("/weather")
def weather(city: str):

    return get_weather(city)


@app.get("/irrigation")
def irrigation(
    crop: str = "",
    soil_type: str = "Loamy",
    soil_moisture: float = 50,
    temperature: float = 25,
    last_rainfall: str = "",
    field_area: float = 1,
    irrigation_method: str = "Flood",
    last_irrigation: str = "",
    weather_condition: str = "normal"
):
    return get_irrigation_recommendation(
        crop, soil_type, soil_moisture, temperature,
        last_rainfall, field_area, irrigation_method,
        last_irrigation, weather_condition
    )

@app.get("/fertilizer")
def fertilizer(
    crop_type: str,
    soil_type: str,
    ph: float,
    n: float,
    p: float,
    k: float,
    area: float,
    stage: str,
    location: str = "",
    previous_fert: str = "",
    irrigation: str = ""
):
    recommendation = predict_fertilizer(crop_type, location, soil_type, ph, n, p, k, area, stage, previous_fert, irrigation)
    return {"recommendation": recommendation}

@app.get("/recommend-crop")
def recommend_crop(
    soil_type: str,
    ph: float,
    temp: float,
    rainfall: float,
    humidity: float,
    n: float,
    p: float,
    k: float,
    location: str,
    season: str
):
    recommended_crop = predict_crop(soil_type, ph, temp, rainfall, humidity, n, p, k, location, season)
    return {"recommended_crop": recommended_crop}


@app.get("/predict-price")
def market_price(
    crop: str,
    month: str,
    demand: str
):

    return predict_market_price(
        crop,
        month,
        demand
    )
