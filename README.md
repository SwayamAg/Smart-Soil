
# 🌾 Smart Soil: Soil Moisture & Crop Prediction Using Satellite Data

### 🔗 [🌐 Live Demo Website](https://soils.vercel.app/)  

---

## 📌 Project Overview  
**Smart Soil** is a geospatial machine learning project that uses **Google Earth Engine (GEE)** and satellite data from **Sentinel-1 & Sentinel-2** to:  
- **Predict Soil Moisture** using NDWI  
- **Classify Crop Types** for agricultural guidance in **India**

The aim is to support farmers with precise insights for better crop planning and irrigation decisions.

---

## 🧪 How the Web App Works (Step-by-Step)

Here’s how to use **Smart Soil** through the website:

### 1️⃣ Register or Sign In
- **Register** for free — one-time only, no charges.
- **Sign In** (if already registered): A small fee of **₹5 per login** applies to help sustain the platform.

### 2️⃣ Allow Location Access
- After login/registration, allow the website to **access your live location**.
- This is required to fetch real-time satellite data for your area.

### 3️⃣ Navigate to Soil Analysis
- Click on the **"Soil Analysis"** tab from the dashboard to begin analysis.
- The backend now starts the data pipeline.

### 4️⃣ Real-Time Satellite Data Extraction
- Your location coordinates are sent to **Google Earth Engine (GEE)**.
- GEE fetches the **latest Sentinel-1 and Sentinel-2 data** for that region.
- Key features like `B4`, `B8`, `NDVI`, `NDWI`, `VH`, and `VV` are extracted.

### 5️⃣ AI-Based Prediction Pipeline
- Extracted features are passed into two trained models:
  - 📉 **Model 1**: Predicts **Soil Moisture Level** (via NDWI)
  - 🌱 **Model 2**: Recommends **best-suited crop** for your location

### 6️⃣ View Results Instantly
- The output screen shows:
  - ✅ **Moisture level** (Low / Medium / High)
  - 🌾 **Recommended crop** for your field

---

## ⚠️ Note on Frontend Code

The frontend code included in this repository **may not fully match** the current live demo website UI and user experience.  
The live demo is actively maintained and updated independently to improve functionality and design.

If you run the app locally, expect a simpler or older UI version that might differ from the deployed web interface.

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
