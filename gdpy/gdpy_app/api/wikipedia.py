import requests
import json
from gdpy.gdpy_app.config import Wiki, Return
import os

params = {
    'action': 'query',  # data extract
    'format': 'json',  # response extension
    'utf8': 1,  # utf-8 conversion (if possible)
    'prop': 'extracts',
    'explaintext': 1,  # more human readable
    'generator': 'geosearch',  # geolocalisation search
    'ggscoord': '0|0',  # default position
    'formatversion': 2
}


class Wikipedia:
    """
        Class to request Wiki Media and save data
    """

    def __init__(self) -> None:
        self.return_value = Return.USER_ERROR
        self.blabla = ''
        self.url = ''

    def req(self, lat: float, lng: float) -> object:
        """
            Request ``lat`` and ``lng`` position to Wiki API
            And save few data (see ``save_data`` method)
            *return: self
        """
        if not isinstance(lat, float) or not isinstance(lng, float):
            return self

        params['ggscoord'] = f'{lat}|{lng}'

        req = requests.get(Wiki.API_URL, params)
        self.save_data(req)

        return self

    def save_data(self, req) -> None:
        """
            From ``req`` request, take and save few data in attributes
        """
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
                    print('Format correct, mais aucune information trouvée.')
                self.return_value = Return.NO_RETURN
            elif response.get('error'):
                self.blabla = response['error']
        else:
            self.return_value = Return.URL_ERROR
