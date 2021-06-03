import wikipedia
import pyttsx3
import speech_recognition as sp

engine = pyttsx3.init()
microfono = sp.Microphone()
riconoscitore = sp.Recognizer()


def parla(frase: str):
    engine.say(frase)
    engine.runAndWait()


if __name__ == '__main__':
    parla("Ciao, cosa vuoi cercare su wikipedia?")
    with microfono as sorgente:
        print("Inizio record")
        audio = riconoscitore.record(sorgente, duration=5)
        print("Fine record")
        ricerca = riconoscitore.recognize_google(audio, language="it_IT")

        wikipedia.set_lang("it")
        result = wikipedia.summary(ricerca, sentences=1)

        parla(result)
