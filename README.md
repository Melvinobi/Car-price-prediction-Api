# Car-price-prediction-Api
Fast api deployment for a car price prediction model
This project demonstrates how to deploy a machine learning regression model as a REST API using FastAPI. The API provides an endpoint for making predictions based on input features.

## Prerequisites

1. Python 3.7 or higher installed.
2. Required Python packages installed (see `requirements.txt`).
3. A trained regression model saved as `linear_regression_model.pkl`.
4. Training data (`X_train`) and corresponding scaler used to preprocess the data.

---

## Setup Instructions

### 1. Clone the Repository
Clone or download the project files to your local machine.

```bash
git clone https://github.com/Melvinobi/Car-price-prediction-Api.git
cd Car-price-prediction-Api
```

### 2. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate   # On Windows
```

Install required packages:

```bash
pip install -r requirements.txt
```

### 3. Ensure Files are Present

Ensure the following files are available in the project folder:

- `app.py`: The main FastAPI application.
- `linear_regression_model.pkl`: The saved model file.
- `requirements.txt`: List of dependencies.

---

## Running the API

### Start the API Server

Run the following command in your terminal:

```bash
python app.py
```

The server will start at `http://127.0.0.1:8000`.

---

## Testing the API

### 1. Verify the API is Running

Open your browser or a tool like Postman and navigate to:

```
http://127.0.0.1:8000
```

You should see the message:

```json
{"message": "Welcome to the car price prediction API"}
```

### 2. Use Swagger UI for Interactive Testing

Navigate to the interactive documentation:

```
http://127.0.0.1:8000/docs
```

Here, you can test the `/predict` endpoint by providing input features as JSON.

### 3. Example Input for `/predict`

Use the following JSON input for testing:

```json
{
  "wheel_base": 88.6,
  "length": 168.8,
  "width": 64.1,
  "engine_size": 130,
  "bore": 3.47,
  "horsepower": 111,
  "city_mpg": 21,
  "make_audi": false,
  "make_bmw": false,
  "make_chevrolet": false,
  "make_dodge": false,
  "make_honda": true,
  "make_jaguar": false,
  "make_mazda": false,
  "make_mercedes_benz": false,
  "make_mitsubishi": false,
  "make_nissan": false,
  "make_peugot": false,
  "make_plymouth": false,
  "make_porsche": false,
  "make_saab": false,
  "make_subaru": false,
  "make_toyota": false,
  "make_volkswagen": false,
  "make_volvo": false,
  "fuel_type_diesel": false,
  "fuel_type_gas": true,
  "body_style_convertible": false,
  "body_style_hardtop": false,
  "body_style_hatchback": false,
  "body_style_sedan": true,
  "body_style_wagon": false,
  "drive_wheels_4wd": false,
  "drive_wheels_fwd": true,
  "drive_wheels_rwd": false,
  "engine_type_dohc": false,
  "engine_type_l": false,
  "engine_type_ohc": true,
  "engine_type_ohcv": false,
  "num_of_cylinders_eight": false,
  "num_of_cylinders_five": false,
  "num_of_cylinders_four": true,
  "num_of_cylinders_six": false,
  "num_of_cylinders_twelve": false
}
```

### 4. Curl Command

You can also test the API using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{
  "wheel_base": 88.6,
  "length": 168.8,
  "width": 64.1,
  "engine_size": 130,
  "bore": 3.47,
  "horsepower": 111,
  "city_mpg": 21,
  "make_audi": false,
  "make_bmw": false,
  "make_chevrolet": false,
  "make_dodge": false,
  "make_honda": true,
  "make_jaguar": false,
  "make_mazda": false,
  "make_mercedes_benz": false,
  "make_mitsubishi": false,
  "make_nissan": false,
  "make_peugot": false,
  "make_plymouth": false,
  "make_porsche": false,
  "make_saab": false,
  "make_subaru": false,
  "make_toyota": false,
  "make_volkswagen": false,
  "make_volvo": false,
  "fuel_type_diesel": false,
  "fuel_type_gas": true,
  "body_style_convertible": false,
  "body_style_hardtop": false,
  "body_style_hatchback": false,
  "body_style_sedan": true,
  "body_style_wagon": false,
  "drive_wheels_4wd": false,
  "drive_wheels_fwd": true,
  "drive_wheels_rwd": false,
  "engine_type_dohc": false,
  "engine_type_l": false,
  "engine_type_ohc": true,
  "engine_type_ohcv": false,
  "num_of_cylinders_eight": false,
  "num_of_cylinders_five": false,
  "num_of_cylinders_four": true,
  "num_of_cylinders_six": false,
  "num_of_cylinders_twelve": false
}'
```

---

## Files in the Repository

1. `app.py`: The main FastAPI application file.
2. `requirements.txt`: Contains the dependencies required for the project.
3. `linear_regression_model.pkl`: The trained regression model.

---

