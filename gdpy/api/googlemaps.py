import requests
import os
import json
from config import Return, Google, DEV
from boto.s3.connection import S3Connection

class GoogleMaps:
    def __init__(self) -> None:
        self.position = {}
        self.formatted_address = ''
        self.return_value = Return.DEFAULT_ERROR

    def req(self, address: str) -> object:
        if DEV == 'TEST':
            google_key = os.getenv("GOOGLE_MAPS_KEY")
        else:
            google_key = S3Connection(os.environ("GOOGLE_MAPS_KEY"))
        params = {
            'address': address,
            'key': google_key
        }

        print('recherche pour :', address)
        req = requests.get(Google.GEOCODE_URL, params)
        self.save_data(req)

        return self

    def save_data(self, req):
        response = json.loads(req.text)
        if req.status_code == 200:
            if response['status'] == Google.STATUS_OK:
                self.position = \
                    response['results'][0]['geometry']['location']
                self.formatted_address = \
                    response['results'][0]['formatted_address']
                self.return_value = Return.RETURN_OK

            elif response['status'] == Google.STATUS_NO_RESULT:
                self.return_value = Return.NO_RETURN
        else:
            self.return_value = Return.URL_ERROR
