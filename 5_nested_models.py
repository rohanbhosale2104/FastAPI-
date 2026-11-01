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

address_info={'city':'New York','state':'NY','street':'123 Main St','zip_code':'10001'}
address1=Address(**address_info) 
patient_info={"name":"John Doe","gender":"Male","address":address1}
patient1=Patient(**patient_info)
print(patient1)
print(patient1.address.city) #this will print the city of the patient's address. The address field in the Patient model is an instance of the Address model, which allows for nested data structures and easy access to the fields of the nested model. 
print(patient1.address.zip_code) #this will print the zip code of the patient's address. The address field in the Patient model is an instance of the Address model, which allows for nested data structures and easy access to the fields of the nested model.


#nested models are useful for representing complex data structures in a clear and organized way. In this example, the Address model is nested within the Patient model, allowing for easy access to the fields of the Address model through the Patient model. This can be useful for representing real-world entities that have multiple attributes and relationships, such as patients and their addresses.
#for example, a patient may have multiple addresses (e.g., home address, work address), and each address may have its own set of attributes (e.g., street, city, state, zip code). By using nested models, we can represent this relationship in a clear and organized way, making it easier to work with the data and perform operations on it.
#if in model having hierarchical data structure then we can use nested models to represent the relationship between the different levels of the hierarchy. For example, a company may have multiple departments, and each department may have multiple employees. By using nested models, we can represent this relationship in a clear and organized way, making it easier to work with the data and perform operations on it.
