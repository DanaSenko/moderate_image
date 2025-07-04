import os
from moderate_service import AI_Service
from traceback import print_tb
from fastapi import FastAPI, File, UploadFile
import requests
import uvicorn
from config import settings
from utils import validate_image

app = FastAPI()

@app.post('/moderate')
def moderate_image(file: UploadFile = File(...)):
    if not validate_image(file):
        return {"status": "ERROR", "reason": "Invalid image format"}
    ai_service = AI_Service()
    return ai_service.moderate_image(file)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)