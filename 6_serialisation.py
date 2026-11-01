from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated  

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name:str
    gender:str
    address: Address

address_dict={'city':'New York','state':'NY','street':'123 Main St','zip_code':'10001'}
address1=Address(**address_dict)
patient_dict={"name":"John Doe","gender":"Male","address":address1}
patient1=Patient(**patient_dict)
# temp=patient1.model_dump(include={'name','gender'}) #this will create a dictionary representation of the Patient model instance, but only include the name and address fields. The model_dump() method is used to convert the model instance to a dictionary format, which can be useful for serialization or for passing data to other functions or APIs that expect a dictionary format.

# temp=patient1.model_dump(exclude={'address'}) #this will create a dictionary representation of the Patient model instance, but exclude the address field. The model_dump() method is used to convert the model instance to a dictionary format, which can be useful for serialization or for passing data to other functions or APIs that expect a dictionary format.

temp=patient1.model_dump(include={'name','address'},exclude={'address':{'zip_code'}}) #this will create a dictionary representation of the Patient model instance, but include the name and address fields, but exclude the zip_code field from the address field. The model_dump() method is used to convert the model instance to a dictionary format, which can be useful for serialization or for passing data to other functions or APIs that expect a dictionary format.



print(temp)

print(type(temp)) #this will print the type of the temp variable, which is a dictionary. The model_dump() method returns a dictionary representation of the Patient model instance, which can be useful for serialization or for passing data to other functions or APIs that expect a dictionary format.