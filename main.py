import gtts
import time
import audioplayer
import speech_recognition

from vocals.service import VocalService
from weather.service import WeatherService


def dirtyVersion():
    tts = gtts.gTTS("Ciao, cosa posso fare per te?", lang="it")
    tts.save("prova.wav")
    audioplayer.AudioPlayer("prova.wav").play(block=True)
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Inizio registrazione...")
        audio = r.record(source, duration=5)
        print("Registrazione terminata.")
    request = r.recognize_google(audio, language="it-IT")
    if "tempo" in request:
        tts = gtts.gTTS("Il tempo sarà buono, domani", lang="it")
        tts.save("prova.wav")
        audioplayer.AudioPlayer("prova.wav").play(block=True)
        time.sleep(1)
    else:
        tts = gtts.gTTS("Mi dispiace, non ho capito", lang="it")
        tts.save("prova.wav")
        audioplayer.AudioPlayer("prova.wav").play(block=True)
    tts = gtts.gTTS("Ciao ciao!", lang="it")
    tts.save("prova.wav")
    audioplayer.AudioPlayer("prova.wav").play(block=True)


def cleanVersion():
    vocalService.saySomething("Ciao, cosa posso fare per te?")
    request = vocalService.listenSomething()
    city = vocalService.findWeatherCityInRequest(request)
    if city is None:
        vocalService.saySomething("Per favore, specifica la città")
        return
    description, temperature = weatherService.getWeatherCity(city)
    weatherPhrase = weatherService.getWeatherPhrase(city, description, temperature)
    vocalService.saySomething(weatherPhrase)


weatherService = WeatherService()
vocalService = VocalService()

if __name__ == '__main__':
    cleanVersion()
