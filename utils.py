import os
import requests

from enum import Enum


class Commons(Enum):
    OWM_FIND_BASE_URL = os.getenv("OWM_FIND_BASE_URL")
    OWM_BASE_URL = os.getenv("OWM_BASE_URL")
    OWM_API_KEY = os.getenv("OWM_API_KEY")
    OWM_FIND_KEY = os.getenv("OWM_FIND_KEY")


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