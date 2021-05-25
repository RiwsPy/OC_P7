import requests
import json

WIKI_URL = "https://fr.wikipedia.org/w/api.php"
WIKI_SEARCH_URL = "https://fr.wikipedia.org/wiki?"
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
        self.url = WIKI_SEARCH_URL

    def req(self, lat, lng):
        params['ggscoord'] = f'{lat}|{lng}'

        req = requests.get(WIKI_URL, params)
        if req.status_code == 200:
            response = json.loads(req.text)
            if response.get('query'):
                # 'title' pour une info résumée
                self.info += response['query']['pages'][0]['extract']
                self.url += f"curid={response['query']['pages'][0]['pageid']}"
                print(self.info[:100])
            elif response.get('batchcomplete') == True:
                print('Format correct, mais aucune information trouvée sur Wiki.')
            elif response.get('error'):
                self.info += response['error']
            else:
                print(response)
        else:
            print('Lien wiki invalide')
        return self
