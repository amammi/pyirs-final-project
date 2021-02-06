import gtts
import time
import audioplayer
import speech_recognition

from vocals.service import VocalService
from weather.service import WeatherService
from wiki.service import WikipediaService


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
    if vocalService.isWeatherRequest(request):
        city = vocalService.findWeatherCityInRequest(request)
        if city is None:
            vocalService.saySomething("Per favore, specifica la città")
            return
        temperature = weatherService.getWeatherCity(city)
        weatherPhrase = weatherService.getWeatherPhrase(city, temperature)
        vocalService.saySomething(weatherPhrase)
    elif vocalService.isWikipediaRequest(request):
        wikiRequest = vocalService.findWikiSentenceInRequest(request.lower())
        if wikiRequest is not None:
            sentence = wikiService.getDetailsOfRequest(wikiRequest)
            if sentence is not None:
                vocalService.saySomething(sentence)
            else:
                vocalService.saySomething("Mi dispiace, ma non ho trovato niente relativo alla tua ricerca.")
        else:
            vocalService.saySomething("Mi dispiace, non ho capito.")
    else:
        vocalService.saySomething("Mi dispiace, non ho capito.")


weatherService = WeatherService()
wikiService = WikipediaService()
vocalService = VocalService()

if __name__ == '__main__':
    cleanVersion()
