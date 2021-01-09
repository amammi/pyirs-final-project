class Temperature(object):
    def __init__(self, actual: int, feels: int, min: int, max: int):
        self.actual = actual
        self.feels = feels
        self.min = min
        self.max = max

    @staticmethod
    def fromJson(jsonData: dict):
        actual = jsonData["temp"]
        feels = jsonData["feels_like"]
        min = jsonData["temp_min"]
        max = jsonData["temp_max"]
        return Temperature(actual, feels, min, max)
