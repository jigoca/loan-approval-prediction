from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib 
import pandas as pd

app = FastAPI()

num_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

model = joblib.load('loan_status_predictor_rf.pkl')
scaler = joblib.load('vector.pkl')

class LoanApproval(BaseModel):
    Gender: float 
    Married: float
    Dependents:float
    Education: float
    Self_Employed: float
    ApplicantIncome:float
    CoapplicantIncome:float
    LoanAmount:float 
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: float


@app.get("/")
def read_root():
    return {"Hola": "Mundo"}

@app.post("/predict")
async def predict_loan_status(application: LoanApproval):
    input_data = pd.DataFrame([application.dict()])
    input_data[num_cols] = scaler.transform(input_data[num_cols])

    result = model.predict(input_data)

    if result[0] == 1:
        return {'Estado del préstamo': "Aprobado"}
    else:
        return {'Estado del préstamo': "No aprobado"}