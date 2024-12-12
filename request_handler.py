from fastapi import FastAPI, HTTPException
import patient_service
from models import PatientModel

app = FastAPI()

@app.get("/patient/{patient_id}")
def patient_details(patient_id: str):
    result = patient_service.get_patient_by_id(patient_id)

    return result

@app.post("/patient")
def add_patient(patient: PatientModel):
    print(patient)
    if not patient_service.add_patient(patient):
        raise HTTPException(status_code=400, detail="Patient already exist")