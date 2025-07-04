import os
from traceback import print_tb
from fastapi import FastAPI, File, UploadFile
import requests
import uvicorn
from config import settings

app = FastAPI()

@app.post('/moderate')
def moderate_image(file: UploadFile = File(...)):
    ai_service = AI_Service()
    return ai_service.moderate_image(file)


class AI_Service:
    def __init__(self):
        self.api_key = str(settings.DEEPAI_API_KEY)
        self.api = 'https://api.deepai.org/api/nsfw-detector'

    def moderate_image(self, file: UploadFile):
        headers = {'Api-Key': self.api_key}
        try:
            response = requests.post(self.api, files={
                'image': file.file
            }, headers=headers)
            try:
                data = response.json()
            except Exception:
                return {"status": "ERROR", "reason": "Invalid JSON in response", "raw_response": response.text, "http_code": response.status_code}
            nsfw_score = data.get('nsfw_score', 0)
            if nsfw_score > 0.7:
                return {"status": "REJECTED", "reason": "NSFW content"}
            else:
                return {"status": "OK"}
        except Exception as e:
            return {"status": "ERROR", "reason": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)