import requests
import json
from config import Wiki, Return
    

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

class Wikipedia:
    def __init__(self) -> None:
        self.data = ''
        self.url = Wiki.DEFAULT_URL
        self.return_value = Return.NO_RETURN

    def req(self, lat: int, lng: int) -> object:
        if not lat or not lng:
            self.return_value = Return.COORD_ERROR
            return self

        params['ggscoord'] = f'{lat}|{lng}'

        req = requests.get(Wiki.URL, params)
        self.save_data(req)

        return self

    def save_data(self, req):
        #with open('mock_wiki_return_ok.json', 'w') as file:
        #    json.dump(json.loads(req.text), file, indent=1, ensure_ascii=False)

        if req.status_code == 200:
            response = json.loads(req.text)
            if response.get('query'):
                # 'title' pour une info résumée
                self.data = response['query']['pages'][0]['extract']
                self.url = Wiki.SEARCH_URL + \
                    f"curid={response['query']['pages'][0]['pageid']}"
                self.return_value = Return.RETURN_OK
                print(self.data[:100])
            elif response.get('batchcomplete') is True:
                print('Format correct, mais aucune information trouvée sur Wiki.')
            elif response.get('error'):
                self.data += response['error']
                self.return_value = Return.DEFAULT_ERROR
            else:
                self.return_value = Return.UNKNOWN_EVENT
                print(response)
        else:
            self.return_value = Return.URL_ERROR
            print('Lien wiki invalide')
