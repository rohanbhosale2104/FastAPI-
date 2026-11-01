from pydantic import BaseModel, EmailStr, AnyUrl, Field,field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:str
    email: EmailStr
    linkedIn: AnyUrl
    age:int
    married: bool
    weight: float
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['hdfc.com', 'icici.com'] #this valid_domains list contains the allowed email domains for the email field. The validate_email method checks if the domain of the provided email address is in this list. If not, it raises a ValueError with a message indicating that the email domain must be one of the valid domains.
        #abc@gmail.com
        domain = value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return value
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value.upper() #this will convert the name to uppercase before storing it in the model. This can be useful for standardizing the format of names in the database or for display purposes.
    
    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        return value

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted successfully")
   
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated successfully") 
    
patient_info={"name":"John Doe","email":"john.doe@hdfc.com","linkedIn":"https://www.linkedin.com/in/johndoe","age":20,"married":False,"weight":70.5,"allergies":["pollen","dust"],"contact_details":{"phone":"123-456-7890","address":"123 Main St"}}
patient1=Patient(**patient_info)
update_patient_data(patient1)