from flask import Flask, request, render_template, jsonify
from gdpy.api.googlemaps import GoogleMaps
from gdpy.api.wikipedia import Wikipedia
from gdpy.parsers import normalize
from gdpy.words import Sentence, NO_POSITION, NO_WIKI
from config import Wiki, Return
from typing import Tuple
from gdpy import app


@app.route('/')
def papy():
    return render_template('papy.html')

@app.route('/api/', methods={'POST'})
def api() -> jsonify:
    wiki_data = None
    result = {}

    user_input = request.data.decode('utf-8')
    maps_data = GoogleMaps().req(normalize(user_input))

    if maps_data.return_value == Return.RETURN_OK:
        lat = maps_data.position.get('lat', 0)
        lng = maps_data.position.get('lng', 0)

        if lat and lng:
            wiki_data = Wikipedia().req(lat, lng)
            result['wiki_url'] = wiki_data.url
            result['position'] = maps_data.position
        else:
            maps_data = None
    else:
        maps_data = None
    result['papy_blabla'] = papy_response(maps_data, wiki_data)

    print(result)
    return jsonify(result)


def papy_response(maps_data: object, wiki_data: object) -> Tuple[str, bool, bool]:
    if maps_data is None:
        return NO_POSITION, False, False

    if wiki_data is None:
        return NO_WIKI, True, False

    papy_text = Sentence().create_random_sentence()
    return f"{papy_text}\r {maps_data.formatted_address} ? {wiki_data.data[:100]}...", True, True


if __name__ == "__main__":
    app.run()
