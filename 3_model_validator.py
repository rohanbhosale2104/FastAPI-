from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict,Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    married: bool
    weight: float
    allergies: Optional[List[str]]
    contact_details: Dict[str,str]
    
    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contacts(cls, model):
        if model.age>60 and 'emergency_contact' not in model.contact_details:
            raise ValueError("Emergency contact is required for patients over 60 years old.")
        # Perform any necessary validation logic here
        return model
    #model validator is a decorator provided by Pydantic that allows you to define custom validation logic for a model. In this case, the validate_emergency_contacts method checks if the age of the patient is greater than 60 and if the contact_details dictionary does not contain an emergency_contact key. If both conditions are met, it raises a ValueError indicating that an emergency contact is required for patients over 60 years old. This ensures that the model adheres to specific validation rules based on the patient's age and contact information.

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted successfully")  
        
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated successfully")   
    
patient_info={"name":"John Doe","email":"john.doe@example.com","age":65,"married":True,"weight":70.5,"allergies":None,"contact_details":{"phone":"123-456-7890","emergency_contact":"234-567-8901"}}

patient1=Patient(**patient_info) #here ** is used to unpack the dictionary patient_info and pass its key-value pairs as keyword arguments to the Patient model. This allows for easy creation of a Patient instance with the provided data. If the data types do not match the expected types defined in the Patient model, Pydantic will raise a validation error.
update_patient_data(patient1)
