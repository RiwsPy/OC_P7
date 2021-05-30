import requests
import json
from config import ERROR_ERROR, ERROR_NO_RETURN, \
    ERROR_RETURN_OK, GOOGLE_MAPS_KEY, GOOGLE_URL, \
    ERROR_URL_ERROR

class GoogleMaps:
    def __init__(self):
        self.lat = 0
        self.lng = 0
        self.formatted_address = ''
        self.return_value = 0

    def req(self, address='1600+Amphitheatre+Parkway,+Mountain+View,+CA'):
        params = {
            'address': address,
            'key': GOOGLE_MAPS_KEY
        }
        print('recherche pour :', address)
        req = requests.get(GOOGLE_URL, params)

        if req.status_code == 200:
            response = json.loads(req.text)
            if response['status'] == 'OK':
                # plusieurs réponses possibles !
                info = response['results'][0]['geometry']['location']
                formatted_address = response['results'][0]['formatted_address']
                self.lat = info['lat']
                self.lng = info['lng']
                self.formatted_address = formatted_address
                self.return_value = ERROR_RETURN_OK
                return self
            elif response['status'] == 'ZERO_RESULTS':
                self.return_value = ERROR_NO_RETURN
                print("Pas connaître !", response)
            else:
                self.return_value = ERROR_ERROR
                print('ERROR', response)
        else:
            self.return_value = ERROR_URL_ERROR
            print('Lien google maps invalide')

        return self
