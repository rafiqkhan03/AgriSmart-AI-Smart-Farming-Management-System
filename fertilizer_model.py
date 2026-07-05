def get_fertilizer_recommendation(
    crop: str,
    nitrogen: str,
    phosphorus: str,
    potassium: str
):

    # Decision Logic

    if nitrogen == "Low":

        fertilizer = (
            "Use Urea fertilizer to increase nitrogen level."
        )

    elif phosphorus == "Low":

        fertilizer = (
            "Use DAP fertilizer to improve phosphorus level."
        )

    elif potassium == "Low":

        fertilizer = (
            "Use NPK fertilizer to increase potassium level."
        )

    else:

        fertilizer = (
            "Soil nutrients are balanced. No fertilizer needed."
        )

    return {

        "crop": crop,
        "nitrogen": nitrogen,
        "phosphorus": phosphorus,
        "potassium": potassium,
        "recommendation": fertilizer

    }