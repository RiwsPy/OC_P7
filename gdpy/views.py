from flask import request, render_template, jsonify
from gdpy.api.googlemaps import GoogleMaps
from gdpy.api.wikipedia import Wikipedia
from gdpy.parsers import normalize
from gdpy.words import Sentence, NO_POSITION, NO_WIKI, NO_GOOGLE, NO_WIKI_INFO
from config import Return
from typing import Tuple
from gdpy import app


@app.route('/')
def papy() -> str:
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

    blabla_1, blabla_2, found_place, found_wiki = \
        papy_response(maps_data, wiki_data)
    result['papy_blabla_1'] = blabla_1
    result['papy_blabla_2'] = blabla_2
    result['found_place'] = found_place
    result['found_wiki'] = found_wiki

    return jsonify(result)


def papy_response(maps_data: object, wiki_data: object) \
        -> Tuple[str, str, bool, bool]:
    """
        From result of Google API (``maps_data``)
        and WikiMedia API (``wiki_data``)
        generate a bot random response and take the decision
        to show maps or wiki link
    """
    second_message = ''
    display_map = False
    display_wiki = False
    if maps_data.return_value in (Return.NO_RETURN, Return.USER_ERROR):
        first_message = NO_POSITION
    elif maps_data.return_value == Return.SERVER_ERROR:
        first_message = NO_GOOGLE
    else:
        display_map = True
        first_message = maps_data.formatted_address
        if wiki_data is None or wiki_data.return_value == Return.NO_RETURN:
            second_message = NO_WIKI_INFO
        elif wiki_data.return_value == Return.USER_ERROR:
            second_message = NO_WIKI

        else:
            papy_text = Sentence().create_random_sentence()
            second_message = f"{papy_text}\r {wiki_data.blabla[:100]}..."
            display_wiki = True

    return first_message, second_message, display_map, display_wiki


if __name__ == "__main__":
    app.run()
