from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}

@app.get("/ping")
def ping():
    return {"status": "alive"}
