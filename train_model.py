# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
# from xgboost import XGBClassifier
# import warnings
# warnings.filterwarnings("ignore")

# # Load dataset
# df = pd.read_csv('Kharif_Dataset_India.csv')  # Replace with actual path

# # Drop unnecessary columns
# if '.geo' in df.columns:
#     df.drop(columns=['.geo', 'system:index'], inplace=True, errors='ignore')

# # Encode crop label
# le_crop = LabelEncoder()
# df['crop'] = le_crop.fit_transform(df['crop'])

# # Bin moisture into labels (customize bins as needed)
# df['moisture_label'] = pd.cut(df['moisture'],
#                                bins=[-1, 10, 20, 40],
#                                labels=['Low', 'Medium', 'High'])

# # Encode moisture labels
# le_moist = LabelEncoder()
# df['moisture_label'] = le_moist.fit_transform(df['moisture_label'])

# # Features and targets
# X = df[['B2', 'B3', 'B4', 'B8']]
# y_moisture = df['moisture_label']
# y_crop = df['crop']

# # Scale features
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # Split data
# X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_scaled, y_moisture, test_size=0.2, random_state=42)
# X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_scaled, y_crop, test_size=0.2, random_state=42)

# # ---------------------------------------------
# # 🌊 Moisture Classification
# # ---------------------------------------------
# def evaluate_classifier(model, name, X_train, y_train, X_test, y_test, label_encoder):
#     model.fit(X_train, y_train)
#     preds = model.predict(X_test)
#     print(f"\n📌 {name} Classification")
#     print("Accuracy:", accuracy_score(y_test, preds))
#     print("Classification Report:\n", classification_report(y_test, preds, target_names=label_encoder.classes_))

# moisture_models = [
# #     (RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42), "Random Forest (Moisture)"),
#     (GradientBoostingClassifier(n_estimators=100, random_state=42), "Gradient Boosting (Moisture)"),
# #     (XGBClassifier(n_estimators=100, random_state=42), "XGBoost (Moisture)")
# ]

# for model, name in moisture_models:
#     evaluate_classifier(model, name, X_train_m, y_train_m, X_test_m, y_test_m, le_moist)

# # ---------------------------------------------
# # 🌾 Crop Classification
# # ---------------------------------------------
# crop_models = [
# #     (RandomForestClassifier(n_estimators=100, random_state=42), "Random Forest (Crop)"),
#     (GradientBoostingClassifier(n_estimators=100, random_state=42), "Gradient Boosting (Crop)"),
# #     (XGBClassifier(n_estimators=100, random_state=42), "XGBoost (Crop)")
# ]

# for model, name in crop_models:
#     evaluate_classifier(model, name, X_train_c, y_train_c, X_test_c, y_test_c, le_crop)






import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import GradientBoostingClassifier
import joblib
import warnings
warnings.filterwarnings("ignore")

# Load dataset
df = pd.read_csv('Kharif_Dataset_India.csv')

# Drop unnecessary columns
df.drop(columns=['.geo', 'system:index'], inplace=True, errors='ignore')

# Encode crop labels
le_crop = LabelEncoder()
df['crop'] = le_crop.fit_transform(df['crop'])

# Bin and encode moisture levels
df['moisture_label'] = pd.cut(df['moisture'], bins=[-1, 10, 20, 40], labels=['Low', 'Medium', 'High'])
le_moist = LabelEncoder()
df['moisture_label'] = le_moist.fit_transform(df['moisture_label'])

# Feature set
X = df[['B2', 'B3', 'B4', 'B8']]
y_moisture = df['moisture_label']
y_crop = df['crop']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_scaled, y_moisture, test_size=0.2, random_state=42)
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_scaled, y_crop, test_size=0.2, random_state=42)

# Moisture model
moisture_model = GradientBoostingClassifier(n_estimators=100, random_state=42)
moisture_model.fit(X_train_m, y_train_m)

# Crop model
crop_model = GradientBoostingClassifier(n_estimators=100, random_state=42)
crop_model.fit(X_train_c, y_train_c)

# Evaluate
print("\n📌 Moisture Classification")
print("Accuracy:", accuracy_score(y_test_m, moisture_model.predict(X_test_m)))
print("Classification Report:\n", classification_report(y_test_m, moisture_model.predict(X_test_m), target_names=le_moist.classes_))

print("\n📌 Crop Classification")
print("Accuracy:", accuracy_score(y_test_c, crop_model.predict(X_test_c)))
print("Classification Report:\n", classification_report(y_test_c, crop_model.predict(X_test_c), target_names=le_crop.classes_))

# Save models and encoders
joblib.dump(moisture_model, 'moisture_model.pkl')
joblib.dump(crop_model, 'crop_model.pkl')
joblib.dump(le_crop, 'crop_label_encoder.pkl')
joblib.dump(le_moist, 'moisture_label_encoder.pkl')
joblib.dump(scaler, 'feature_scaler.pkl')

print("\n✅ Models and encoders saved successfully.")

