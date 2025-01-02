import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score, mean_squared_error
import joblib  # For saving and loading the model

# Load dataset (modify the path if needed)
data = pd.read_csv('dataset.csv')

# Ensure 'skills' column is numeric (if needed, otherwise skip this step)
data['skills'] = data['skills'].astype(int)

# Feature columns and target columns
X = data.drop(['eligibility', 'salary'], axis=1)  # Features (removing eligibility and salary)
y_classification = data['eligibility']  # Target for classification (binary)
y_regression = data['salary']  # Target for regression (continuous)

# Apply scaling to all numeric columns
scaler = StandardScaler()
X_scaled = X.copy()
# Apply scaling to numeric columns only
X_scaled = pd.DataFrame(scaler.fit_transform(X_scaled), columns=X.columns)

# Split the dataset into training and testing sets
X_train, X_test, y_train_class, y_test_class = train_test_split(X_scaled, y_classification, test_size=0.2, random_state=42)
_, _, y_train_reg, y_test_reg = train_test_split(X_scaled, y_regression, test_size=0.2, random_state=42)

# Train a Random Forest Classifier for eligibility (classification)
model_classification = RandomForestClassifier(random_state=42)
model_classification.fit(X_train, y_train_class)

# Evaluate the classification model
y_pred_class = model_classification.predict(X_test)
print("Accuracy (Classification):", accuracy_score(y_test_class, y_pred_class))
print("Classification Report:\n", classification_report(y_test_class, y_pred_class))

# Train a Random Forest Regressor for salary (regression)
model_regression = RandomForestRegressor(random_state=42)
model_regression.fit(X_train, y_train_reg)

# Evaluate the regression model
y_pred_reg = model_regression.predict(X_test)
print("Mean Squared Error (Regression):", mean_squared_error(y_test_reg, y_pred_reg))

# Save the classification model
model_classification_file_path = "model_classification.joblib"
joblib.dump(model_classification, model_classification_file_path)
print(f"Classification model saved to {model_classification_file_path}")

# Save the regression model
model_regression_file_path = "model_regression.joblib"
joblib.dump(model_regression, model_regression_file_path)
print(f"Regression model saved to {model_regression_file_path}")

# Save the scaler to preprocess new data consistently
scaler_file_path = "scaler.pkl"
joblib.dump(scaler, scaler_file_path)
print(f"Scaler saved to {scaler_file_path}")

