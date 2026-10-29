from fastapi import FastAPI,Path,HTTPException,Query
import json

app=FastAPI() #object of FastAPI class

def load_data():
    with open("patients.json",'r') as f:
        data=json.load(f)
    return data
@app.get("/") #decorator
def hello():
    return {"message":"Patient Management System System API."}

@app.get("/about")
def about():
    return {"message":"A fully functional API to manage your Patient Records."}

@app.get("/view")
def view():
    data=load_data()
    return data

@app.get("/patient/{patient_id}")
def get_patient(patient_id:str=Path(...,description="The ID of the patient in the DB",example="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404,detail="Patient not Found.")
    
@app.get("/sort")
def sort_patients(sort_by:str=Query(...,description="sort on the basis of height,weight,bmi"),order:str=Query("asc",description="sort in ascending or desceding order")):
    valid_fields=["height","weight","bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Invalid Field Select from {valid_fields}")
        #status code 400 means bad request
    if order not in ["asc","desc"]:
        raise HTTPException(status_code=400,detail="Invalid Order Select from ['asc','desc']")
    data=load_data()
    sort_order=True if order=="desc" else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data
    
    