import wikipedia


class WikipediaService:

    def __init__(self):
        wikipedia.set_lang("it")

    def getNaiveSummary(self, request: str):
        try:
            result = wikipedia.summary(request, sentences=2)
            return result
        except wikipedia.DisambiguationError:
            return None

    def getDetailsOfRequest(self, request: str, results: list = None) -> str:
        try:
            if results is None:
                results = wikipedia.search(request)
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



