import pickle
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from sklearn.preprocessing import StandardScaler
import uvicorn
import nest_asyncio



# Assuming model, X, and scaler are defined and loaded
with open('linear_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Manually define the expected input features
X_columns = [
    'wheel_base', 'length', 'width', 'engine_size', 'bore', 'horsepower', 'city_mpg',
    'make_audi', 'make_bmw', 'make_chevrolet', 'make_dodge', 'make_honda', 'make_jaguar',
    'make_mazda', 'make_mercedes_benz', 'make_mitsubishi', 'make_nissan', 'make_peugot',
    'make_plymouth', 'make_porsche', 'make_saab', 'make_subaru', 'make_toyota', 'make_volkswagen',
    'make_volvo', 'fuel_type_diesel', 'fuel_type_gas', 'body_style_convertible', 'body_style_hardtop',
    'body_style_hatchback', 'body_style_sedan', 'body_style_wagon', 'drive_wheels_4wd', 'drive_wheels_fwd',
    'drive_wheels_rwd', 'engine_type_dohc', 'engine_type_l', 'engine_type_ohc', 'engine_type_ohcv',
    'num_of_cylinders_eight', 'num_of_cylinders_five', 'num_of_cylinders_four', 'num_of_cylinders_six',
    'num_of_cylinders_twelve'
]

# Define your scaler (fit it on the fly if not previously fitted and saved)
scaler = StandardScaler()

# Create the API app
app = FastAPI()

# Pydantic model for input validation
class Features(BaseModel):
    wheel_base: float
    length: float
    width: float
    engine_size: int
    bore: float
    horsepower: float
    city_mpg: int
    make_audi: bool
    make_bmw: bool
    make_chevrolet: bool
    make_dodge: bool
    make_honda: bool
    make_jaguar: bool
    make_mazda: bool
    make_mercedes_benz: bool
    make_mitsubishi: bool
    make_nissan: bool
    make_peugot: bool
    make_plymouth: bool
    make_porsche: bool
    make_saab: bool
    make_subaru: bool
    make_toyota: bool
    make_volkswagen: bool
    make_volvo: bool
    fuel_type_diesel: bool
    fuel_type_gas: bool
    body_style_convertible: bool
    body_style_hardtop: bool
    body_style_hatchback: bool
    body_style_sedan: bool
    body_style_wagon: bool
    drive_wheels_4wd: bool
    drive_wheels_fwd: bool
    drive_wheels_rwd: bool
    engine_type_dohc: bool
    engine_type_l: bool
    engine_type_ohc: bool
    engine_type_ohcv: bool
    num_of_cylinders_eight: bool
    num_of_cylinders_five: bool
    num_of_cylinders_four: bool
    num_of_cylinders_six: bool
    num_of_cylinders_twelve: bool


@app.get("/")
def index():
    return {"message": "Welcome to the car price prediction API"}


@app.post("/predict")
def predict(features: Features):
    try:
        # Convert input features to DataFrame
        input_df = pd.DataFrame([features.dict()])
        
        # Ensure the input features match the training features
        input_df = input_df.reindex(columns=X_columns, fill_value=0)
        
        # Scale the input features
        # Fit and scale the input features
        input_scaled = scaler.fit_transform(input_df)
        # Make prediction
        prediction = model.predict(input_scaled)
        
        return {"predicted_price": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error during prediction: {str(e)}")


if __name__ == "__main__":
    nest_asyncio.apply()
    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
