import joblib
import numpy as np

# -------------------------------
# Load Saved Models and Scaler
# -------------------------------
moisture_model = joblib.load('moisture_model.pkl')
crop_model = joblib.load('crop_model.pkl')

# Optionally, load your scaler if used earlier and saved separately
# If you didn't save it, you can refit StandardScaler again on original dataset
from sklearn.preprocessing import StandardScaler

# Sample band values (you can change these)
# Format: [B2, B3, B4, B8]
sample_input = np.array([[120.5, 135.2, 115.8, 180.3]])

# If you used StandardScaler before training, apply the same here
scaler = StandardScaler()
# Fit with sample values just for demo purposes (in real app, use the real scaler)
scaler.fit(sample_input)
X_scaled = scaler.transform(sample_input)

# -------------------------------
# Predict
# -------------------------------
moisture_pred = moisture_model.predict(X_scaled)[0]
crop_pred = crop_model.predict(X_scaled)[0]

# Optional: Decode labels manually (based on original encoding)
moisture_labels = ['Low', 'Medium', 'High']
crop_labels = ['Bajra', 'Cotton', 'Maize', 'Paddy', 'Pulses', 'Soybean']  # Replace with your actual crop names in order

print(f"\n🌊 Predicted Moisture Level: {moisture_labels[moisture_pred]}")
print(f"🌾 Predicted Crop Recommendation: {crop_labels[crop_pred]}")
