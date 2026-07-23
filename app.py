from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("car_price_model.pkl")
scaler = joblib.load("scaler.pkl")

class CarData(BaseModel):
    Symboling: float
    Normalized_Losses: float
    Wheel_Base: float
    Length: float
    Width: float
    Height: float
    Curb_Weight: float
    Engine_Size: float
    Bore: float
    Stroke: float
    Horsepower: float
    Peak_RPM: float
    City_mpg: float

    Fuel_Type_gas: int
    Aspiration_std: int
    No_of_Doors_four: int

    Body_Style_hardtop: int
    Body_Style_hatchback: int
    Body_Style_sedan: int
    Body_Style_wagon: int

    Drive_Wheels_fwd: int

    Engine_Location_front: int

    Engine_Type_dohc: int
    Engine_Type_l: int
    Engine_Type_ohc: int
    Engine_Type_ohcf: int
    Engine_Type_ohcv: int

    No_of_Cylinders_eight: int
    No_of_Cylinders_five: int
    No_of_Cylinders_four: int
    No_of_Cylinders_six: int
    No_of_Cylinders_two: int

    Fuel_System_1bbl: int
    Fuel_System_2bbl: int
    Fuel_System_mpfi: int
    Fuel_System_spdi: int

@app.get("/")
def home():
    return {"message": "Car Price Prediction API is Ready!"}

@app.post("/predict")
def predict(data: CarData):

    input_data = [[
        data.Symboling,
        data.Normalized_Losses,
        data.Wheel_Base,
        data.Length,
        data.Width,
        data.Height,
        data.Curb_Weight,
        data.Engine_Size,
        data.Bore,
        data.Stroke,
        data.Horsepower,
        data.Peak_RPM,
        data.City_mpg,
        data.Fuel_Type_gas,
        data.Aspiration_std,
        data.No_of_Doors_four,
        data.Body_Style_hardtop,
        data.Body_Style_hatchback,
        data.Body_Style_sedan,
        data.Body_Style_wagon,
        data.Drive_Wheels_fwd,
        data.Engine_Location_front,
        data.Engine_Type_dohc,
        data.Engine_Type_l,
        data.Engine_Type_ohc,
        data.Engine_Type_ohcf,
        data.Engine_Type_ohcv,
        data.No_of_Cylinders_eight,
        data.No_of_Cylinders_five,
        data.No_of_Cylinders_four,
        data.No_of_Cylinders_six,
        data.No_of_Cylinders_two,
        data.Fuel_System_1bbl,
        data.Fuel_System_2bbl,
        data.Fuel_System_mpfi,
        data.Fuel_System_spdi
    ]]

    scaled_data = scaler.transform(input_data)

    prediction = model.predict(scaled_data)

    return {
        "Predicted Price": float(prediction[0])
    }