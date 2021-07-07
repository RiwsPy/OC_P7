from views import papy_response
from gdpy.words import NO_POSITION, NO_WIKI

class Map_data:
    def __init__(self) -> None:
        self.formatted_address = 'test'

class Wiki_data:
    def __init__(self) -> None:
        self.data = 'blablabla'

def test_papy_response():
    maps_data = None
    wiki_data = None
    ret = papy_response(maps_data, wiki_data)
    assert ret == (NO_POSITION, False, False)

    maps_data = Map_data()
    ret = papy_response(maps_data, wiki_data)
    assert ret == (NO_WIKI, True, False)

    wiki_data = Wiki_data()
    ret = papy_response(maps_data, wiki_data)
    assert ret[1]
    assert ret[2]
    assert type(ret[0]) is str
    assert wiki_data.data[:100] in ret[0]
    assert maps_data.formatted_address in ret[0]
