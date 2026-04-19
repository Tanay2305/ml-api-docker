from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

@app.get("/")   #route url endpoint
def home():     
    return {"message":"Hello from docker API"}  #json response

@app.get("/predict")
def predict(num: int):
    result = model.predict([[num]])
    return {"result": result[0]}

