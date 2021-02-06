from utils import NetworkHelper
import wikipedia


class WikipediaService(NetworkHelper):

    def __init__(self):
        wikipedia.set_lang("it")

    def getDetailsOfRequest(self, request: str, results: list = None) -> str:
        try:
            print(request)
            if results is None:
                results = wikipedia.search(request)
                print(results)
                result = wikipedia.summary(results[0], sentences=2)
            else:
                result = wikipedia.summary(results[0], sentences=2)
            return result
        except wikipedia.DisambiguationError:
            if len(results) > 0:
                results.pop(0)
                self.getDetailsOfRequest(request, results)
            else:
                return None


if __name__ == '__main__':
    print(wikipedia.search("new York")[0])