from flask import request, render_template, jsonify
from gdpy.gdpy_app.api.googlemaps import GoogleMaps
from gdpy.gdpy_app.api.wikipedia import Wikipedia
from gdpy.gdpy_app.parsers import normalize
from gdpy.gdpy_app.words import Sentence, NO_POSITION, NO_WIKI, NO_GOOGLE, \
    NO_WIKI_INFO, I_HAVE_THE_RESPONSE
from gdpy.gdpy_app.config import Return
from typing import Tuple
from gdpy.website import app


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
        result['position'] = maps_data.position

        wiki_data = Wikipedia().req(**maps_data.position)
        if wiki_data.return_value == Return.RETURN_OK:
            result['wiki_url'] = wiki_data.url

    result['papy_blabla_1'], result['papy_blabla_2'], \
        result['found_place'], result['found_wiki'] = \
        papy_response(maps_data, wiki_data)

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
        first_message = I_HAVE_THE_RESPONSE + maps_data.formatted_address
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
