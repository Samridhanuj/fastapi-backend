from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class DataRequest(BaseModel):
    data: List[str]

@app.get("/")
async def root():
    return {"message": "FastAPI is running"}

@app.post("/bfhl")
async def process_data(request: DataRequest):
    user_id = "SamridhAnuj10"
    email = "samridhanuj10@gmail.com"
    roll_number = "22BCS10640"

    numbers = [item for item in request.data if item.isdigit()]
    alphabets = [item for item in request.data if item.isalpha()]
    highest_alphabet = [max(alphabets, key=lambda x: x.upper())] if alphabets else []

    return {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}
