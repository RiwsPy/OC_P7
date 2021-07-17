"""
    Test the module gdpy/api/googlemaps.py
"""

import requests
from gdpy.api.googlemaps import GoogleMaps, Return
import json
import os


class Mock_requests:
    def __init__(self, status_code, position_found=True) -> None:
        self.status_code = status_code
        self.text = ''
        self.position_found = position_found
# requests.models.Response


def requests_get(mock) -> object:
    if mock.status_code == 200:
        if mock.position_found:
            filename = '/mock_googlemaps_return.json'
        else:
            filename = '/mock_googlemaps_return_no_found.json'
    else:
        filename = '/mock_googlemaps_return_void.json'

    with open(os.path.join(os.path.dirname(__file__)) + filename, 'r') as file:
        mock.text = file.read()
    return mock


def test_req_ok(monkeypatch):
    with open(
            os.path.join(os.path.dirname(__file__)) +
            '/mock_googlemaps_return.json',
            'r') as file:

        test_data = json.load(file)

    mock = Mock_requests(200)

    def Mock_requests_get(*args, **kwargs):
        return requests_get(mock)
    monkeypatch.setattr(requests, 'get', Mock_requests_get)

    data = GoogleMaps().req('Pétra')
    assert data.position == \
        test_data['results'][0]['geometry']['location']
    assert data.formatted_address == \
        test_data['results'][0]['formatted_address']
    assert data.return_value == Return.RETURN_OK


def test_req_void(monkeypatch):
    mock = Mock_requests(400)

    def Mock_requests_get(*args, **kwargs):
        return requests_get(mock)
    monkeypatch.setattr(requests, 'get', Mock_requests_get)

    data = GoogleMaps().req('')
    assert not data.position
    assert not data.formatted_address
    assert data.return_value == Return.URL_ERROR


def test_req_no_found(monkeypatch):
    mock = Mock_requests(200, position_found=False)

    def Mock_requests_get(*args, **kwargs):
        return requests_get(mock)
    monkeypatch.setattr(requests, 'get', Mock_requests_get)

    data = GoogleMaps().req('dkjfndsjfdjsfjfnrn')
    assert not data.position
    assert not data.formatted_address
    assert data.return_value == Return.NO_RETURN
