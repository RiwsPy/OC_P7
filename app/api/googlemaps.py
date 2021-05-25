import requests
import json
from config import GOOGLE_MAPS_KEY, GOOGLE_URL

def init(address='1600+Amphitheatre+Parkway,+Mountain+View,+CA'):
    # nécessite une conversion des espaces en + etc ? > ou pas
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
            #print(response['results'][0])
            return info['lat'], info['lng'], formatted_address
        elif response['status'] == 'ZERO_RESULTS':
            print("Pas connaître !", response)
        else:
            print('ERROR', response)
    else:
        print('Lien google maps invalide')
    return None, None, None

