# AgriSmart-AI-Smart-Farming-Management-System
An AI-powered Smart Farming Management System built with FastAPI, Python, MySQL, and Machine Learning. The platform provides an interactive dashboard for smart agriculture, Live wether, Plant Disease Detection, smart irrigation planner, Crop and Fertilizer reccomendation



# 🌱 AgriSmart – AI Smart Farming Management System

AgriSmart is an AI-powered Smart Farming Management System built using **Python**, **FastAPI**, **Machine Learning**, **Deep Learning**, and **MySQL**. It is designed to assist farmers and agricultural enthusiasts by providing intelligent recommendations and real-time insights for better farming decisions.

The system integrates AI models with a modern web interface to deliver features such as crop recommendation, plant disease detection, smart irrigation planning, fertilizer recommendation, live weather updates, and an interactive dashboard.

---

## 🚀 Features

### 👤 User Authentication
- User Registration
- Secure Login System
- Admin Login Support

---

### 📊 Interactive Dashboard

A clean and responsive dashboard that provides access to all smart farming tools.

**Dashboard Features**
- 🌱 Crop Recommendation
- 🍃 Plant Disease Detection
- 💧 Smart Irrigation Planner
- 🌿 Fertilizer Recommendation
- 🌦 Live Weather
- 📄 Disease Prediction History
- 📥 Export Prediction Reports (CSV)

---

### 🌱 Crop Recommendation

Recommends the most suitable crop based on agricultural conditions.

The recommendation system considers:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Soil Conditions

This helps users choose crops that are better suited to the available soil nutrients.

---

### 🍃 Plant Disease Detection

Uses a Deep Learning model to detect plant diseases from uploaded leaf images.

**Features**
- Upload Plant Leaf Image
- Disease Classification
- Prediction Confidence Score
- Prediction History
- CSV Report Export

---

### 💧 Smart Irrigation Planner

Provides irrigation recommendations based on multiple farming parameters.

The recommendation considers:

- Crop Type
- Soil Type
- Soil Moisture
- Temperature
- Previous Rainfall
- Weather Conditions
- Irrigation Method

The system also generates irrigation alerts to help optimize water usage.

---

### 🌿 Fertilizer Recommendation

Suggests suitable fertilizers according to soil nutrient levels.

Parameters used:

- Nitrogen
- Phosphorus
- Potassium

The recommendation helps improve soil fertility and crop growth.

---

### 🌦 Live Weather Information

Retrieves real-time weather data using the OpenWeather API.

Weather details include:

- Temperature
- Humidity
- Wind Speed
- Weather Condition
- Irrigation Alert

---

### 📄 Disease Prediction Reports

Users can export plant disease prediction history as a CSV report for analysis and record keeping.

---

## 🧠 AI Models Used

### Machine Learning
- Crop Recommendation Model

### Deep Learning
- Plant Disease Detection using TensorFlow (MobileNetV2)

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI

### Frontend
- HTML5
- CSS3
- JavaScript

### Database
- MySQL

### Machine Learning & Deep Learning
- TensorFlow
- MobileNetV2
- NumPy
- Pandas

### APIs
- OpenWeather API

---

## 📂 Project Structure

```
AgriSmart/
│
├── backend/
│   ├── user_model.py
│   ├── crop_model.py
│   ├── dashboard_model.py
│   ├── disease_model.py
│   ├── fertilizer_model.py
│   ├── irrigation_model.py
│   ├── prediction_model.py
│   └── weather_model.py
│
├── ml_models/
│   ├── train_disease_model.py
│   ├── detect_disease.py
│   └── recommendation_model.py
│
├── frontend/
│   ├── login.html
│   ├── signup.html
│   ├── index.html
│   └── admin.html
│
├── uploads/
├── database/
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AgriSmart-AI-Smart-Farming-Management-System.git
```

### 2. Navigate to the Project Directory

```bash
cd AgriSmart-AI-Smart-Farming-Management-System
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Server

```bash
uvicorn main:app --reload
```

### 5. Open the Application

```
http://127.0.0.1:8000
```

---

## 📸 Screenshots

> Add screenshots here before publishing the repository.

- Login Page
- Signup Page
- Dashboard
- Crop Recommendation
- Disease Detection
- Irrigation Planner
- Fertilizer Recommendation
- Weather Dashboard
- Admin Dashboard

---

## 🚀 Future Improvements

- IoT Sensor Integration
- Mobile Application
- Cloud Deployment
- Multi-language Support
- Advanced AI Models
- User Profile Management
- Advanced Analytics Dashboard
- Satellite Image Integration

---

## 👨‍💻 Author

**Fazil Rafiq**

B.Tech – Computer Science & Engineering

Aspiring AI & Data Science Engineer

LinkedIn: *(Add your LinkedIn Profile)*

GitHub: *(Add your GitHub Profile)*

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub if you found it useful.

---

## 📄 License

This project is developed for educational, learning, and portfolio purposes.
