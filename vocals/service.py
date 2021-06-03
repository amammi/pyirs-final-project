import pyttsx3
import speech_recognition as sr


class VocalService(object):
    def __init__(self):
        """
        Inizializza i moduli per fare lo speech e l'ascolto
        """
        # ---- Configurazione del modulo pyttsx3 ---- #
        self.engine = pyttsx3.init(driverName="nsss")
        self.engine.setProperty("volume", 1.0)
        self.engine.setProperty('rate', 160)

        # ---- Configurazione del modulo SpeechRecognition ---- #
        self.microphone = sr.Microphone()
        self.recognizer = sr.Recognizer()
        self.lang = "it_IT"

    def saySomething(self, phrase: str):
        """
        Metodo per far parlare il computer
        :param phrase: la frase da far dire al computer
        :return: None
        """
        self.engine.say(phrase)
        self.engine.runAndWait()

    def listenSomething(self, duration: int = 5) -> str:
        """
        Metodo per far ascoltare il pc e trascrivere tutto in una stringa
        :param duration: durata (in secondi) di ascolto
        :return: la stringa trascritta oppure None
        """
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Inizio registrazione...")
            record = self.recognizer.record(source, duration=duration)
            print("Fine registrazione")
            return self.recognizer.recognize_google(record, language=f"{self.lang}")

    def isWikipediaRequest(self, sentence: str):
        """
        Metodo utile per capire se dalla frase detta, vogliamo cercare o meno su Wikipedia
        :param sentence: la frase trascritta
        :return: True se 'Wikipedia' è all'interno della frase detta oppure False
        """
        return "wikipedia" in sentence.lower()

    def findWikiSentenceInRequest(self, sentence: str) -> str:
        """
        Metodo per trovare l'oggetto della nostra richiesta su Wikipedia
        :param sentence: la frase pronunciata dall'utente e trascritta
        :return: la parte della stringa contenente la ricerca da effettuare
        """
        tokens = sentence.lower().split(" ")
        try:
            index = tokens.index("wikipedia")
            return " ".join(tokens[index + 1:])
        except ValueError:
            return None

    def isPositiveSentence(self, sentence: str) -> bool:
        """
        Metodo utile per capire se l'utente ha detto si oppure no
        :param sentence: la frase pronunciata
        :return: True se la frase contiente "sì", altrimenti False
        """
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
