import requests
import json
from config import WIKI_URL, WIKI_SEARCH_URL, WIKI_DEFAULT_URL, \
    ERROR_ERROR, ERROR_NO_RETURN, ERROR_RETURN_OK, ERROR_UNKNOWN_EVENT, \
    ERROR_URL_ERROR, ERROR_COORD_ERROR

params = {
    'action': 'query', # extraction des données
    'format': 'json', # format de la réponse
    'utf8': 1, # formatage en utf-8 (si possible)
    'prop': 'extracts',
    'explaintext': 1, # convertion en un texte plus lisible
    'generator': 'geosearch', # recherche par géolocalisation
    'ggscoord': '0|0', # position

    'formatversion': 2

}

class Wiki:
    def __init__(self):
        self.info = ''
        self.url = WIKI_DEFAULT_URL
        self.return_value = ERROR_NO_RETURN

    def req(self, lat, lng):
        if not lat:
            self.return_value = ERROR_COORD_ERROR
            return self

        params['ggscoord'] = f'{lat}|{lng}'

        req = requests.get(WIKI_URL, params)
        if req.status_code == 200:
            response = json.loads(req.text)
            if response.get('query'):
                # 'title' pour une info résumée
                self.info = response['query']['pages'][0]['extract']
                self.url += f"curid={response['query']['pages'][0]['pageid']}"
                self.return_value = ERROR_RETURN_OK
                print(self.info[:100])
            elif response.get('batchcomplete') == True:
                print('Format correct, mais aucune information trouvée sur Wiki.')
            elif response.get('error'):
                self.info += response['error']
                self.return_value = ERROR_ERROR
            else:
                self.return_value = ERROR_UNKNOWN_EVENT
                print(response)
        else:
            self.return_value = ERROR_URL_ERROR
            print('Lien wiki invalide')
        return self
