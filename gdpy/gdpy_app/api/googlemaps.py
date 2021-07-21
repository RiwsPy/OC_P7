import requests
import os
import json
from config import Return, Google


class GoogleMaps:
    """
        One class to request GoogleMaps and save data
    """
    def __init__(self) -> None:
        self.return_value = Return.USER_ERROR
        self.position = {}
        self.formatted_address = ''

    def req(self, address: str) -> object:
        """
            Request ``adress`` to Google API geocoding
            And save few data (see ``save_data`` method)
            *return: self
        """
        params = {
            'address': address,
            'region': 'FR',  # region influence
            'key': os.getenv("GOOGLE_MAPS_KEY")
        }

        if os.getenv('DEV_PHASE') == 'TEST':
            print('recherche pour :', address)
        req = requests.get(Google.GEOCODE_URL, params)
        self.save_data(req)

        return self

    def save_data(self, req) -> None:
        """
            From ``req`` request, take and save few data in attributes
        """
        response = json.loads(req.text)
        if req.status_code == 200:
            google_status = Google.Status(response['status'])
            if google_status.is_ok:
                self.position = \
                    response['results'][0]['geometry']['location']

                if self.position == {'lng': 0, 'lat': 0}:
                    self.return_value = Return.NO_RETURN
                else:
                    self.formatted_address = \
                        response['results'][0]['formatted_address']
                    self.return_value = Return.RETURN_OK

            elif google_status == Google.Status.ZERO_RESULTS:
                self.return_value = Return.NO_RETURN
            elif google_status.is_error_from_server:
                self.return_value = Return.SERVER_ERROR
        else:
            self.return_value = Return.URL_ERROR
