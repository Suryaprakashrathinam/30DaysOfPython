from fastapi import FastAPI
from model import UserRegistration  # make sure your file is named model.py

app = FastAPI()

# Optional home route (uncomment if you want a homepage message)
@app.get("/")
def home():
    return {"message": "Welcome to the Event Registration API 🎉"}

# Registration endpoint
@app.post("/register/")
def register_user(user: UserRegistration):
    return {
        "message": "Registration Successful!",
        "user": user
    }
