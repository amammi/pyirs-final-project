class Temperature(object):
    def __init__(self, description: str, jsonData: dict):
        self.description = ""
        self.actual = .0
        self.feels = .0
        self.min = .0
        self.max = .0
        self.fromJson(description, jsonData)

    def fromJson(self, description: str, jsonData: dict):
        self.description = description
        self.actual = jsonData["temp"]
        self.feels = jsonData["feels_like"]
        self.min = jsonData["temp_min"]
        self.max = jsonData["temp_max"]
