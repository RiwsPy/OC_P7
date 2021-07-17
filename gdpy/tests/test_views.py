from gdpy.views import papy_response
from gdpy.words import NO_GOOGLE, NO_POSITION, NO_WIKI, NO_WIKI_INFO
from gdpy.api.wikipedia import Wikipedia
from gdpy.api.googlemaps import GoogleMaps
from config import Return

def test_papy_response_no_google():
    maps_data = GoogleMaps()
    wiki_data = Wikipedia()
    ret = papy_response(maps_data, wiki_data)
    assert ret == (NO_POSITION, '', False, False)

    maps_data.return_value = Return.SERVER_ERROR
    ret = papy_response(maps_data, wiki_data)
    assert ret == (NO_GOOGLE, '', False, False)

def test_papy_response_google_ok_but_no_wiki():
    wiki_data = Wikipedia()
    maps_data = GoogleMaps()
    maps_data.return_value = Return.RETURN_OK

    ret = papy_response(maps_data, wiki_data)
    assert ret[1:] == (NO_WIKI, True, False)

    wiki_data.return_value = Return.NO_RETURN
    ret = papy_response(maps_data, wiki_data)
    assert ret[1:] == (NO_WIKI_INFO, True, False)

def test_papy_response_both_api_are_ok():
    wiki_data = Wikipedia()
    maps_data = GoogleMaps()
    wiki_data.return_value = Return.RETURN_OK
    maps_data.return_value = Return.RETURN_OK
    wiki_data.blabla = 's<iuvhvuidshufhfuhquffvslsufguzeeh'
    maps_data.formatted_address = 'Paris, France'

    ret = papy_response(maps_data, wiki_data)
    assert maps_data.formatted_address == ret[0]
    assert wiki_data.blabla[:100] in ret[1]
    assert ret[2]
    assert ret[3]
