from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema import CarFeatures, PredictionResponse
from model import predict_price, load_artifacts

app = FastAPI(title="Car Price Prediction API")

@app.on_event("startup")
def startup_event():
    load_artifacts()


@app.get("/")
def test():
    return JSONResponse(status_code=200, content={"Success": True, "message": "This is test route"})


@app.post("/predict", response_model=PredictionResponse)
def predict(features: CarFeatures):
    price = predict_price(features.model_dump())
    return PredictionResponse(prediction_price=price)