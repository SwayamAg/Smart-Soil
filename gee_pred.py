import ee
import joblib
import numpy as np
import os

# -------- GEE Auth --------
service_account = 'hackaccino@swaoil.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, 'swaoil-9a2d2d61f006.json')
ee.Initialize(credentials)

# -------- Load Models & Encoders --------
moisture_model = joblib.load('moisture_model.pkl')
crop_model = joblib.load('crop_model.pkl')
scaler = joblib.load('feature_scaler.pkl')
crop_encoder = joblib.load('crop_label_encoder.pkl')
moisture_encoder = joblib.load('moisture_label_encoder.pkl')

# -------- Check if point is inside India --------
def is_point_in_india(lat, lon):
    india = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017") \
        .filter(ee.Filter.eq('country_na', 'India'))
    point = ee.Geometry.Point([lon, lat])
    return india.filterBounds(point).size().getInfo() > 0

# -------- GEE Fetch Function --------
def get_band_values(lat, lon):
    point = ee.Geometry.Point([lon, lat])

    image = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED') \
        .filterBounds(point) \
        .filterDate('2023-01-01', '2023-12-31') \
        .sort('CLOUDY_PIXEL_PERCENTAGE') \
        .first()

    if image is None:
        return None

    bands = image.select(['B2', 'B3', 'B4', 'B8'])
    values = bands.reduceRegion(
        reducer=ee.Reducer.first(),
        geometry=point,
        scale=10
    ).getInfo()

    return values

# -------- Main Prediction Function --------
def predict_from_location(lat, lon):
    if not is_point_in_india(lat, lon):
        return {"error": "Location is outside of India."}

    band_values = get_band_values(lat, lon)
    if not band_values or None in band_values.values():
        return {"error": "Satellite data unavailable or cloudy for this location."}

    try:
        features = np.array([[band_values['B2'], band_values['B3'], band_values['B4'], band_values['B8']]])
        features_scaled = scaler.transform(features)

        # Predict moisture and crop
        predicted_moisture_encoded = moisture_model.predict(features_scaled)[0]
        predicted_crop_encoded = crop_model.predict(features_scaled)[0]

        # Decode the predictions using label encoders
        predicted_moisture = moisture_encoder.inverse_transform([predicted_moisture_encoded])[0]
        predicted_crop = crop_encoder.inverse_transform([predicted_crop_encoded])[0]

        return {
            "input_bands": band_values,
            "moisture_level": predicted_moisture,
            "recommended_crop": predicted_crop
        }

    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}

# -------- Manual Test --------
if __name__ == "__main__":
    lat = 28 # use geo-location api
    lon = 77 # use geo-location api
    result = predict_from_location(lat, lon)
    print(result)
