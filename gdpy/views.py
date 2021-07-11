from flask import request, render_template, jsonify
from gdpy.api.googlemaps import GoogleMaps
from gdpy.api.wikipedia import Wikipedia
from gdpy.parsers import normalize
from gdpy.words import Sentence, NO_POSITION, NO_WIKI, NO_GOOGLE, NO_WIKI_INFO
from config import Return
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
        lat = maps_data.position['lat']
        lng = maps_data.position['lng']

        wiki_data = Wikipedia().req(lat, lng)
        if wiki_data.return_value == Return.RETURN_OK:
            result['wiki_url'] = wiki_data.url
            result['position'] = maps_data.position

    result['papy_blabla'] = papy_response(maps_data, wiki_data)

    return jsonify(result)


def papy_response(maps_data: object, wiki_data: object) -> Tuple[str, bool, bool]:
    if maps_data.return_value in (Return.NO_RETURN, Return.USER_ERROR):
        return NO_POSITION, False, False
    elif maps_data.return_value == Return.SERVER_ERROR:
        return NO_GOOGLE, False, False

    if wiki_data is None or wiki_data.return_value == Return.NO_RETURN:
        return NO_WIKI_INFO, True, False
    elif wiki_data.return_value == Return.USER_ERROR:
        return NO_WIKI, True, False

    papy_text = Sentence().create_random_sentence()
    return f"{papy_text}\r {maps_data.formatted_address} ? {wiki_data.blabla[:100]}...", True, True


if __name__ == "__main__":
    app.run()
