from fastapi import FastAPI, File, Query, UploadFile, HTTPException, Form
from fastapi.responses import FileResponse, PlainTextResponse
import uvicorn
import joblib
import numpy as np
from pydantic import BaseModel


app = FastAPI(
    title="Insurance Claims Fraud Detection API",
    description="""An API that utilises a Machine Learning model that detects if a if an insurance claim is fraudulent or not based on the following features: hours, amount, transaction type etc.""",
    version="1.0.0", debug=True)


model = joblib.load('auto_claims_fraud.pkl')

@app.get("/", response_class=PlainTextResponse)
async def running():
  note = """
Insurance Claims Fraud Detection API 🙌🏻
Note: add "/docs" to the URL to get the Swagger UI Docs or "/redoc"
  """
  return note

@app.get('/')
def home():
    return {'Title': 'Insurance Claims Fraud Detection API'}


																	
class detectFraud(BaseModel):
    AccidentArea: object
    PoliceReportFiled: object
    WitnessPresent: object
    AgentType: object
    BasePolicy: object
    FraudFound: int	
   

@app.post('/predict')
def predict(data: detectFraud):
                                                                                                                                                                                                                                
    features = np.array([[data.AccidentArea, data.PoliceReportFiled, data.WitnessPresent, data.AgentType, data.FraudFound]])
    model = joblib.load('auto_claims_fraud.pkl')

    predictions = model.predict(features)
    if predictions == 1:
        return {"fraudulent"}
    elif predictions == 0:
        return {"valid"}






