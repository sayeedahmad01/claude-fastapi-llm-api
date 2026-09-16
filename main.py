from fastapi import FastAPI  
import json

app = FastAPI()

#lets create helper function to read ptient records from a file
def load_data():
      with open("patients.json", "r") as f:
            data = json.load(f)
      return data

@app.get("/")
def hello():
    return {"message": "Hello, World!"}  

@app.get("/sayeed_ahmad")
def sayeed_ahmad():
      return {"message": "This is a FastAPI application created by sayeed ahmad."}

@app.get("/patient_record")
def patient_record():
      return {"message": "This is a FastAPI application to manage patient records."}

@app.get("/view")
def view():
      data = load_data()
      return data