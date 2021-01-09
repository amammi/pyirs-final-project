from gtts import gTTS
import audioplayer
import speech_recognition as sr


class VocalService(object):
    def __init__(self):
        self.microphone = sr.Microphone()
        self.recognizer = sr.Recognizer()
        self.lang = "it"
        self.filename = "prova.wav"

    def saySomething(self, phrase: str):
        vocal = gTTS(phrase, lang=self.lang)
        vocal.save(self.filename)
        player = audioplayer.AudioPlayer(self.filename)
        player.play(block=True)

    def listenSomething(self, duration: int = 5) -> str:
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Inizio registrazione...")
            record = self.recognizer.record(source, duration=duration)
            print("Fine registrazione")
            return self.recognizer.recognize_google(record, language=f"{self.lang}_IT")

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
