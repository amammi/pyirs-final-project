import pyttsx3
import speech_recognition as sr


class VocalService(object):
    def __init__(self):
        self.engine = pyttsx3.init(driverName="nsss")
        self.engine.setProperty("volume", 1.0)
        self.engine.setProperty('rate', 150)

        self.microphone = sr.Microphone()
        self.recognizer = sr.Recognizer()
        self.lang = "it_IT"

    def saySomething(self, phrase: str):
        self.engine.say(phrase)
        self.engine.runAndWait()

    def listenSomething(self, duration: int = 5) -> str:
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Inizio registrazione...")
            record = self.recognizer.record(source, duration=duration)
            print("Fine registrazione")
            return self.recognizer.recognize_google(record, language=f"{self.lang}")

    def isWikipediaRequest(self, sentence: str):
        return "wikipedia" in sentence or "Wikipedia" in sentence

    def findWikiSentenceInRequest(self, request: str) -> str:
        tokens = request.split(" ")
        try:
            index = tokens.index("wikipedia")
            return " ".join(tokens[index + 1:])
        except ValueError:
            return None

    def isPositiveSentence(self, sentence: str) -> bool:
        return "si" in sentence.lower() or "sì" in sentence.lower()

    def isWeatherRequest(self, request: str):
        return "tempo" in request

    def findWeatherCityInRequest(self, request: str) -> str:
        if self.isWeatherRequest(request):
            tokens = request.split(" ")
            try:
                index = tokens.index("a")
                return tokens[index + 1]
            except ValueError:
                return None
        else:
            return None
