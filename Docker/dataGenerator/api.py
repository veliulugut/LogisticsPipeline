from fastapi import FastAPI, HTTPException
from dataGenerator import generate_mock_data
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Welcome to Logistics API"}

@app.get("/generate_data")
def generate_data():
    try:
        data = generate_mock_data()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8088)
