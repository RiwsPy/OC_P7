from app.api.wikipedia import Wikipedia
import os
import json
from config import Return, Wiki
from app.api.wikipedia import Wikipedia, params
import requests

class Mock_requests:
    def __init__(self, status_code, position_found=True) -> None:
        self.status_code = status_code
        self.text = ''
        self.url = ''
        self.position_found = position_found
# requests.models.Response

def requests_get(mock) -> object:
    if mock.status_code == 200:
        filename = '/mock_wiki_return_ok.json'

    with open(os.path.join(os.path.dirname(__file__)) + filename, 'r') as file:
        mock.text = file.read()
    return mock

def test_req_ok(monkeypatch):
    with open(os.path.join(os.path.dirname(__file__)) + \
            '/mock_wiki_return_ok.json', 'r') as file:
        test_data = json.load(file)

    mock = Mock_requests(200)
    def Mock_requests_get(*args, **kwargs):
        return requests_get(mock)
    monkeypatch.setattr(requests, 'get', Mock_requests_get)

    lat = 30.3284544
    lng = 35.4443622
    data = Wikipedia().req(f'{lat}|{lng}', params)
    assert data.return_value == Return.RETURN_OK
    assert data.url == Wiki.SEARCH_URL + "curid=5351"
