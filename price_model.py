def predict_market_price(
    crop: str,
    month: str,
    demand: str
):

    # Base price for crops

    base_prices = {

        "Rice": 2200,
        "Wheat": 2100,
        "Maize": 1800,
        "Potato": 1500,
        "Tomato": 2000,
        "Onion": 1700,
        "Cotton": 5500,
        "Sugarcane": 3000,
        "Soybean": 4000

    }

    # Get base price

    price = base_prices.get(
        crop,
        2000
    )

    # Month adjustment

    if month in ["June", "July", "August"]:

        price += 200

    elif month in ["December", "January"]:

        price += 150

    # Demand adjustment

    if demand == "High":

        price += 300

    elif demand == "Low":

        price -= 200

    return {

        "crop": crop,
        "month": month,
        "demand": demand,
        "predicted_price": price

    }