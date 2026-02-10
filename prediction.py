import random

classes = ["Acne", "Eczema", "Psoriasis"]

def predict_disease(image):
    disease = random.choice(classes)
    confidence = round(random.uniform(80, 98), 2)
    return disease, confidence
