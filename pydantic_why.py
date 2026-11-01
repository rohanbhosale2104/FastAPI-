# def insert_patient_data(name:str,age:int):
#     if type(age) is not int:
#         raise ValueError("Age must be an integer.")
#     if type(name) is not str:
#         raise ValueError("Name must be a string.")
#     print(name)
#     print(age)
#     print("Patient data inserted successfully.")
#insert_patient_data("John Doe", 70) #in this code will run successfully because the age parameter is expected to be an integer, but a string is passed. This will not raise an error in Python, but it may lead to unexpected behavior if the function relies on age being an integer for further processing.


from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    # name: str=field(min_length=50) #name must be at least 50 characters long
    name:Annotated[str,Field(max_length=50,title="Patient Name",description="The name of the patient",example="John Doe")] #name must be at least 50 characters long and also field is giving custom metadata for the name field, including a title, description, and example value. This can be useful for documentation purposes or for generating API documentation.
    email: EmailStr
    linkedIn: AnyUrl
    age: Annotated[int,Field(gt=0,lt=120,title="Patient Age",description="The age of the patient in years",example=30,strict=True)] #age must be greater than 0 and less than 120. The field function is used to provide additional metadata for this field, including a title, description, and example value and strict is used for type checking otherwise it will not raise an error.
    married: Annotated[bool,Field(title="Marital Status",description="Indicates whether the patient is married or not",default=False)] #married field is a boolean that indicates whether the patient is married or not. The field function is used to provide additional metadata for this field, including a title, description, and example value.
    weight: Annotated[float,Field(gt=0,title="Patient Weight",description="The weight of the patient in kilograms",example=70.5)] #weight must be greater than 0
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=20)] #if the patient has no allergies, this field can be left empty or set to None.
    contact_details: Dict[str,str]
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted successfully")
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated successfully")

patient_info={"name":"John Doe","email":"john.doe@example.com","linkedIn":"https://www.linkedin.com/in/johndoe","age":23,"married":False,"weight":70.5,"allergies":["pollen","dust"],"contact_details":{"phone":"123-456-7890","address":"123 Main St"}}
patient1=Patient(**patient_info) #here ** is used to unpack the dictionary patient_info and pass its key-value pairs as keyword arguments to the Patient model. This allows for easy creation of a Patient instance with the provided data. If the data types do not match the expected types defined in the Patient model, Pydantic will raise a validation error.
# insert_patient_data(patient1) 
update_patient_data(patient1) 