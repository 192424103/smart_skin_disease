def recommend_care(disease):
    recommendations = {
        "Acne": "Use salicylic acid cleanser and avoid oily products.",
        "Eczema": "Apply moisturizer daily and avoid harsh soaps.",
        "Psoriasis": "Use medicated creams and consult dermatologist."
    }

    return recommendations.get(disease, "Consult a dermatologist.")
