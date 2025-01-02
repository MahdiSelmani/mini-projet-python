import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load("candidate_suitability_model.joblib")
scaler = joblib.load("scaler.pkl")

# Example input data for a candidate (years_of_experience, similarity, skills)
candidate_data = np.array([[1, 1, 0]])

# Scale the input data using the same scaler used during training
scaled_data = scaler.transform(candidate_data)

# Make the prediction
prediction = model.predict(scaled_data)

# Output the result
if prediction[0] == 1:
    print("The candidate is eligible.")
else:
    print("The candidate is not eligible.")