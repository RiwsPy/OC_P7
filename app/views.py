from flask import Flask, request, render_template, jsonify
from app.api.googlemaps import GoogleMaps
from app.api.wikipedia import Wikipedia
from app.parsers import normalize
from app.words import Sentence, NO_POSITION, NO_WIKI
from config import Wiki, Return
from typing import Tuple
from app import app


def init():
    app.run()
    app.config.from_object('config')

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


"""
@app.errorhandler(404)
def page_404(error):
    return f"Page introuvable. ERROR 404 by me", 404

@app.route('/animaux/')
def animaux():
    return render_template('animaux.html')

@app.route('/contact/', methods={'GET', 'POST'})
# il est possible de générer deux routes distinctes :
# @app.route('/contact/', methods={'GET'})
# @app.route('/contact/', methods={'POST'})
def truc():
    mail = 't.d@mail.fr'
    adr = '222 NickonNiki'
    return f'{mail}, {adr} {request.path} {request.method} {dir(request)} {request.get_json}'
"""
if __name__ == "__main__":
    app.run()
