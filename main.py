from fastapi import FastAPI

app=FastAPI() #object of FastAPI class
@app.get("/") #decorator
def hello():
    return {"message":"Hello World"}

@app.get("/about")
def about():
    return {"message":"This is a FastAPI application."}