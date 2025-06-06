# 🌾 Smart Soil: Soil Moisture & Crop Prediction Using Satellite Data

### 🔗 [🌐 Live Demo Website](https://soils.vercel.app/)  

---

## 📌 Project Overview  
**Smart Soil** is a geospatial machine learning project that uses **Google Earth Engine (GEE)** and satellite data from **Sentinel-1 & Sentinel-2** to:  
- **Predict Soil Moisture** using NDWI  
- **Classify Crop Types** for agricultural guidance in **India**

The aim is to support farmers with precise insights for better crop planning and irrigation decisions.

---

## 🛠️ Technologies Used
- **Python**: NumPy, Pandas, Scikit-learn, XGBoost, Matplotlib
- **Google Earth Engine (GEE)**: Satellite data extraction
- **Machine Learning**: Random Forest, XGBoost
- **Joblib**: Model serialization
- **Web Demo**: Vercel and Onrender 

---

## 📊 Dataset Details
- **Source**: Satellite imagery from Sentinel-1 & Sentinel-2 processed via GEE  
- **Features Extracted**:
  - Bands: `B4`, `B8`, `B11`, `B12` (Sentinel-2), `VH`, `VV` (Sentinel-1)
  - Indices: `NDVI`, `NDWI`
  - Latitude, Longitude
  - Labels: Crop types & soil moisture levels

---

## 🧠 Model Overview

### 🟫 1. Soil Moisture Prediction (Regression)
- **Model**: XGBoost Regressor  
- **Target**: NDWI  
- **Performance**:
  - ✅ MSE: `0.0001`
  - ✅ R² Score: `0.9675`

### 🌾 2. Crop Type Classification (Multi-Class)
- **Model**: Random Forest Classifier  
- **Classes**: Millets, Wheat, Barley, Sugarcane, Rice, Jute  
- **Performance**:
  - ✅ Accuracy: `99.9%`
  - ✅ Precision/Recall/F1: `99.9%`

---

## 📁 Folder Structure
```
Agro_Sphere/
├── agrosphere/                  # Core app or modules
├── auth.py                      # GEE authentication
├── gee_pred.py                  # Satellite feature fetch via GEE
├── train_model.py               # Unified training script
├── predict.py                   # Unified prediction script
├── crop_model.pkl               # Crop classification model
├── moisture_model.pkl           # Soil moisture regression model
├── *_label_encoder.pkl          # Label encoders
├── feature_scaler.pkl           # Feature scaler
├── requirements.txt             # Dependencies
├── swaoil-****.json             # (Private) GEE auth key (not public)
└── README.md
```

---

## 🚀 How to Run Locally

1. **Clone the Repository**
```bash
git clone https://github.com/SwayamAg/Agro_Sphere.git
cd Agro_Sphere
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Run Predictions**
```bash
python predict.py
```

> ⚠️ _Ensure you’ve set up your GEE service account (`auth.py`) and JSON file correctly._

---

## 🌐 Live Demo Website

🟢 Check out the deployed web app:  
**🔗 [Smart-Soil](https://soils.vercel.app/)**  
Use the interface to:
- Upload satellite feature data
- Get real-time soil moisture predictions
- Receive crop recommendations

---

## 🔮 Future Scope
- 🌍 Expand coverage to multiple states in India  
- 📲 Launch mobile version for offline use  
- 📡 Add real-time satellite sync via APIs  
- 🧠 Integrate weather forecasts for dynamic recommendations

---

## ✨ Contributor
- **Swayam Agarwal**  
  AI/ML | Earth Observation | Generative AI

---

## 📄 License
Licensed under the [MIT License](LICENSE).

---

### 🌱 Empowering Agriculture with AI, One Pixel at a Time!
