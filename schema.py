from pydantic import BaseModel, Field
from enum import Enum


class FuelType(str, Enum):
    petrol = "Petrol"
    diesel = "Diesel"
    cng = "CNG"

class SellerType(str, Enum):
    dealer = "Dealer"
    invidual = "Invidual"

class TransmissionType(str, Enum):
    manual = "Manual"
    automatic = "Automatic"

class CarFeatures(BaseModel):
    Car_Name : str = Field(..., example="ritz")
    Year : int = Field(..., example=2018)
    Present_Price : float = Field(..., example=5.59)
    Kms_Driven : int = Field(..., example=27000)
    Fuel_Type: FuelType
    Seller_Type: SellerType
    Transmission: TransmissionType
    Owner : int = Field(..., ge=0,le=3, example=0, description="Number of Previous Owners(0-3)")


class PredictionResponse(BaseModel):
    prediction_price: float






