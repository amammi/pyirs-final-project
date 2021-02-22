import os
import requests

from enum import Enum


class Commons(Enum):
    OWM_FIND_BASE_URL = os.getenv("OWM_FIND_BASE_URL")
    OWM_BASE_URL = os.getenv("OWM_BASE_URL")
    OWM_API_KEY = os.getenv("OWM_API_KEY")
    OWM_FIND_KEY = os.getenv("OWM_FIND_KEY")


class VocalSentencies(Enum):
    VOCAL_ERROR_MESSAGE = "Mi dispiace, non ho capito."
    VOCAL_ERROR_NOT_FOUND = "Mi dispiace, ma non ho trovato niente relativo alla tua ricerca."
    VOCAL_CITY_NOT_FOUND = "Per favore, specifica la città"
    VOCAL_GREETING = "Ciao, cosa posso fare per te?"
    VOCAL_ANOTHER_REQUEST = "Vuoi effettuare una nuova ricerca?"
    VOCAL_BYE_BYE = "Ciao e a presto!"


class NetworkHelper(object):
    def __init__(self, baseUrl: str):
        self.baseUrl = baseUrl

    @staticmethod
    def insert_api_key(result: str):
        return result + f"appid={Commons.OWM_API_KEY.value}"

    @staticmethod
    def insert_find_api_key(result: str):
        return result + f"appid={Commons.OWM_FIND_KEY.value}"

    def get(self, params: dict) -> dict:
        result = self.baseUrl +"?"
        for k, v in params.items():
            result += f"{k}={v}&"
        if "isFindCall" not in params.keys() or not params["isFindCall"]:
            result = NetworkHelper.insert_api_key(result)
        else:
            result = NetworkHelper.insert_find_api_key(result)
        response = requests.get(result)
        data = response.json()
        return data