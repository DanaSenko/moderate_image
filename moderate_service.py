from fastapi import UploadFile
import requests
from config import settings

class AI_Service:
    RAPIDAPI_KEY = settings.RAPIDAPI_KEY
    RAPIDAPI_HOST = "nsfw3.p.rapidapi.com"
    API_URL = "https://nsfw3.p.rapidapi.com/v1/results"

    def moderate_image(self, file: UploadFile) -> dict:
        headers = {
            "x-rapidapi-key": self.RAPIDAPI_KEY,
            "x-rapidapi-host": self.RAPIDAPI_HOST,
        }
        files = {"image": file.file}
        response = requests.post(self.API_URL, headers=headers, files=files)
        data = response.json()

        results = data.get("results", [])
        if not results:
            return {"status": "ERROR", "reason": "No results in response"}

        entities = results[0].get("entities", [])
        if not entities:
            return {"status": "ERROR", "reason": "No entities in response"}

        classes = entities[0].get("classes", {})
        nsfw_score = classes.get("nsfw", 0)
        if nsfw_score > 0.7:
            return {"status": "REJECTED", "reason": "NSFW content"}
        else:
            return {"status": "OK"}