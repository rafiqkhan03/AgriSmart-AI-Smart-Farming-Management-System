def get_irrigation_recommendation(
    crop: str,
    soil_type: str,
    soil_moisture: float,
    temperature: float,
    last_rainfall: str,
    field_area: float,
    irrigation_method: str,
    last_irrigation: str,
    weather_condition: str = "normal"
):
    crop = crop.strip().lower() if crop else "general crop"
    soil_type = soil_type.strip() if soil_type else "Loamy"
    irrigation_method = irrigation_method.strip() if irrigation_method else "Flood"
    weather_lower = weather_condition.lower()

    # ── Urgency & Water Requirement ──
    if soil_moisture < 25:
        urgency = "🚨 Critical — Irrigate Immediately"
        urgency_color = "#f87171"
        water_need = "High"
        irrigation_today = True
        moisture_msg = "Soil moisture is critically low. Crops are under severe water stress."
    elif soil_moisture < 40:
        urgency = "⚠️ Low — Irrigation Needed Soon"
        urgency_color = "#fbbf24"
        water_need = "Moderate–High"
        irrigation_today = True
        moisture_msg = "Soil moisture is below optimal. Plan irrigation within the next 24 hours."
    elif soil_moisture <= 65:
        urgency = "✅ Moderate — Monitor Closely"
        urgency_color = "#34d399"
        water_need = "Low–Moderate"
        irrigation_today = False
        moisture_msg = "Soil moisture is in an acceptable range. Light irrigation may help, especially in hot weather."
    else:
        urgency = "🚫 High — Do Not Irrigate"
        urgency_color = "#38bdf8"
        water_need = "None"
        irrigation_today = False
        moisture_msg = "Soil is already saturated. Over-irrigation can cause root rot and nutrient leaching."

    # ── Rain override ──
    rain_keywords = ["rain", "drizzle", "shower", "thunderstorm"]
    has_rain = any(kw in weather_lower for kw in rain_keywords) or "rain" in (last_rainfall or "").lower()

    if has_rain and irrigation_today:
        urgency = "🌧️ Delay — Rain Detected"
        urgency_color = "#60a5fa"
        irrigation_today = False
        delay_note = "⚠️ Rain is expected or recently occurred. Delay irrigation to avoid over-watering and nutrient runoff."
    else:
        delay_note = None

    # ── Temperature advisory ──
    if temperature > 40:
        temp_advice = "Extreme heat! Water early morning (5–7 AM) or after sunset to minimise evaporation losses."
    elif temperature > 35:
        temp_advice = "High temperature detected. Irrigate in the early morning or evening to reduce evaporation."
    elif temperature < 15:
        temp_advice = "Cool temperatures slow evaporation. Reduce irrigation frequency and quantity."
    else:
        temp_advice = "Temperature is moderate. Standard irrigation timing (morning) is ideal."

    # ── Water quantity per acre (approximate, in litres) ──
    base_litres_per_acre = {
        "Drip": 1500,
        "Flood": 4000,
        "Sprinkler": 2500,
        "Furrow": 3500,
        "Manual": 1200,
    }
    base = base_litres_per_acre.get(irrigation_method, 2500)

    # Moisture adjustment
    moisture_factor = max(0.3, (100 - soil_moisture) / 100)
    litres_per_acre = round(base * moisture_factor)
    total_litres = round(litres_per_acre * (field_area or 1))

    # ── Soil-type specific advice ──
    soil_advice_map = {
        "Clay":  "Clay soil retains water well but drains slowly. Avoid over-irrigation. Use shorter, more frequent sessions.",
        "Sandy": "Sandy soil drains very quickly. Increase irrigation frequency. Drip irrigation is highly recommended.",
        "Loamy": "Loamy soil is ideal — good water retention and drainage. Standard irrigation is effective.",
        "Black": "Black (vertisol) soil expands when wet and cracks when dry. Keep consistent moisture to prevent cracking.",
        "Red":   "Red laterite soil drains fast and has low water retention. Increase irrigation frequency.",
        "Silty": "Silty soil compacts easily. Avoid heavy flood irrigation — prefer drip or sprinkler methods.",
    }
    soil_advice = soil_advice_map.get(soil_type, "Maintain consistent soil moisture for optimal crop growth.")

    # ── Method-specific tip ──
    method_tips = {
        "Drip":      "Drip irrigation delivers water directly to roots — up to 50% more efficient than flood. Ideal for most crops.",
        "Flood":     "Flood irrigation is simple but uses the most water. Ensure levelled field to avoid waterlogging in low spots.",
        "Sprinkler": "Sprinklers cover large areas evenly. Best used in the morning to allow leaf surfaces to dry before evening.",
        "Furrow":    "Furrow irrigation works well for row crops. Ensure furrows are not too long to prevent uneven distribution.",
        "Manual":    "Manual irrigation is labour-intensive. Consider upgrading to drip or sprinkler for large field areas.",
    }
    method_tip = method_tips.get(irrigation_method, "Choose an efficient irrigation method suited to your crop and soil type.")

    # ── Schedule suggestion ──
    next_irrigation = "Tomorrow morning (6–8 AM)" if irrigation_today else "In 2–3 days — check soil moisture again"
    if has_rain:
        next_irrigation = "After the rain clears — check soil moisture before irrigating"

    return {
        "urgency": urgency,
        "urgency_color": urgency_color,
        "water_need": water_need,
        "irrigation_today": irrigation_today,
        "moisture_msg": moisture_msg,
        "delay_note": delay_note,
        "temp_advice": temp_advice,
        "litres_per_acre": litres_per_acre,
        "total_litres": total_litres,
        "soil_advice": soil_advice,
        "method_tip": method_tip,
        "next_irrigation": next_irrigation,
        "crop": crop.title(),
        "field_area": field_area or 1,
        "irrigation_method": irrigation_method,
        "soil_moisture": soil_moisture,
        "temperature": temperature,
    }