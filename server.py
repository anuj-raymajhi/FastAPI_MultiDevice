# device2.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    data: str

@app.post("/process-data/")
async def process_data(data: Data):
    # Simulate data preprocessing
    preprocessed_data = data.data.upper()  # Example preprocessing
    return {"preprocessed_data": preprocessed_data}