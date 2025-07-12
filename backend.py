def predict_pcos(age, weight, cycle, symptoms):
    risk_score = 0

    if weight > 70:
        risk_score += 1
    if cycle == "Irregular":
        risk_score += 2
    if "Facial hair" in symptoms:
        risk_score += 1
    if "Acne" in symptoms:
        risk_score += 1
    if "Hair loss" in symptoms:
        risk_score += 1

    if risk_score >= 3:
        return "High Risk of PCOS"
    elif risk_score == 2:
        return "Moderate Risk"
    else:
        return "Low Risk"
