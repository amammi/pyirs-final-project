import gtts
import time
import audioplayer
import speech_recognition

from utils import Commons, VocalSentencies
from vocals.service import VocalService
# from weather.service import WeatherService
from wiki.service import WikipediaService


def main():
    listening = True
    while listening:
        vocalService.saySomething(VocalSentencies.VOCAL_GREETING.value)
        request = vocalService.listenSomething()

        if vocalService.isWikipediaRequest(request):
            wikiRequest = vocalService.findWikiSentenceInRequest(request.lower())
            if wikiRequest is not None:
                sentence = wikiService.getNaiveSummary(wikiRequest)
                if sentence is not None:
                    vocalService.saySomething(sentence)
                else:
                    vocalService.saySomething(VocalSentencies.VOCAL_ERROR_NOT_FOUND.value)
            else:
                vocalService.saySomething(VocalSentencies.VOCAL_ERROR_MESSAGE.value)
        # elif vocalService.isWeatherRequest(request):
        #     city = vocalService.findWeatherCityInRequest(request)
        #     if city is None:
        #         vocalService.saySomething(VocalSentencies.VOCAL_CITY_NOT_FOUND.value)
        #         return
        #     temperature = weatherService.getWeatherCity(city)
        #     weatherPhrase = weatherService.getWeatherPhrase(city, temperature)
        #     vocalService.saySomething(weatherPhrase)
        else:
            vocalService.saySomething(VocalSentencies.VOCAL_ERROR_MESSAGE.value)
        vocalService.saySomething(VocalSentencies.VOCAL_ANOTHER_REQUEST.value)
        response = vocalService.listenSomething(duration=2)
        listening = vocalService.isPositiveSentence(response)
    vocalService.saySomething(VocalSentencies.VOCAL_BYE_BYE.value)


# weatherService = WeatherService()
wikiService = WikipediaService()
vocalService = VocalService()

if __name__ == '__main__':
    main()
