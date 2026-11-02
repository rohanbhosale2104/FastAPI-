from fastapi import FastAPI, HTTPException,Path, Query, Body
from pydantic import BaseModel,Field,computed_field
from typing import Optional,Annotated,Literal
from fastapi.responses import JSONResponse
import json

app=FastAPI()

class Patient(BaseModel):
    id:Annotated[str, Field(...,title="Patient ID", description="Unique identifier for the patient",example="P12345")]
    name:Annotated[str, Field(...,title="Patient Name", description="Full name of the patient",example="John Doe")]
    city:Annotated[str, Field(...,title="City", description="City where the patient resides",example="New York")]
    age:Annotated[int, Field(...,gt=0,lt=150,title="Age", description="Age of the patient in years",example=30)]
    gender:Annotated[Literal["Male", "Female", "Other"], Field(...,title="Gender", description="Gender of the patient",example="Male")]
    height:Annotated[float, Field(...,gt=0,title="Height", description="Height of the patient in centimeters",example=175.5)]
    weight:Annotated[float, Field(...,gt=0,title="Weight", description="Weight of the patient in kilograms",example=70.5)]
    
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)
    
    @computed_field
    @property   
    def bmi(self) -> float:
        """Calculate the Body Mass Index (BMI) of the patient."""
        height_in_meters = self.height / 100  # Convert height from cm to meters
        bmi = round(self.weight / (height_in_meters ** 2), 2)  # Calculate BMI and round to 2 decimal places
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        """Determine the BMI category based on the calculated BMI."""
        bmi = self.bmi
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"
    
@app.post('/create')
def create_patient(patient: Patient):
    #load existing data
    data=load_data()
    
    #check if patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail=f"Patient with ID {patient.id} already exists.")
    
    #new patient add to the database
    data[patient.id] = patient.model_dump(exclude={'id'})  # Ensure the patient data is in dictionary format
    save_data(data)
    return JSONResponse(content={"message": f"Patient with ID {patient.id} created successfully."}, status_code=201)
    

  
