import requests
import json
from config import Wiki, Return
import os

params = {
    'action': 'query', # data extract
    'format': 'json', # response extension
    'utf8': 1, # utf-8 conversion (if possible)
    'prop': 'extracts',
    'explaintext': 1, # more human readable
    'generator': 'geosearch', # geolocalisation search
    'ggscoord': '0|0', # default position

    'formatversion': 2

}

class Wikipedia:
    def __init__(self) -> None:
        self.return_value = Return.DEFAULT_ERROR
        self.blabla = ''
        self.url = ''

    def req(self, lat: int, lng: int) -> object:
        if not isinstance(lat, float) or not isinstance(lng, float):
            self.return_value = Return.USER_ERROR
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
                self.blabla = response['query']['pages'][0]['extract']
                self.url = Wiki.SEARCH_URL + \
                    f"curid={response['query']['pages'][0]['pageid']}"
                self.return_value = Return.RETURN_OK
            elif response.get('batchcomplete') is True:
                if os.getenv('DEV_PHASE') == 'TEST':
                    print('Format correct, mais aucune information trouvée sur Wiki.')
                self.return_value = Return.NO_RETURN
            elif response.get('error'):
                self.blabla = response['error']
                self.return_value = Return.USER_ERROR
            else:
                self.return_value = Return.USER_ERROR
        else:
            self.return_value = Return.URL_ERROR
