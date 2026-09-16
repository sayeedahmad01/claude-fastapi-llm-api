from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/sayeed_ahmad")
def sayeed_ahmad():
    return {"message": "Hello, Sayeed Ahmad!"}