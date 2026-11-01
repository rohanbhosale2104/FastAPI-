from pydantic import BaseModel, EmailStr, AnyUrl, Field,computed_field
from typing import List, Dict, Optional, Annotated  

class Patient(BaseModel):
    name:str
    email: EmailStr
    age:int
    married: bool
    weight: float
    height: float
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi=round(self.weight / (self.height ** 2), 2) #this will calculate the BMI of the patient based on their weight and height. The BMI is calculated by dividing the weight in kilograms by the square of the height in meters. This computed field can be accessed like any other attribute of the Patient model, but it is not stored in the database or serialized when the model is converted to JSON.
        return bmi

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted successfully")      
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("BMI:", patient.bmi) #this will print the BMI of the patient when the update_patient_data function is called. The BMI is calculated using the computed_field bmi defined in the Patient model."
    print("updated successfully")

patient_info={"name":"John Doe","email":"john.doe@example.com","age":30,"married":True,"weight":70.5,"height":1.75,"allergies":["peanuts"],"contact_details":{"phone":"123-456-7890","address":"123 Main St"}}

patient1=Patient(**patient_info)

update_patient_data(patient1)