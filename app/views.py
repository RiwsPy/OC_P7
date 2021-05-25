from flask import Flask, request, make_response, render_template, jsonify
from app.api import googlemaps, wikipedia
from app.parsers import normalize

app = Flask(__name__)
app.debug = True

def init():
    app.run()

@app.route('/contact/', methods={'GET', 'POST'})
# il est possible de générer deux routes distinctes :
# @app.route('/contact/', methods={'GET'})
# @app.route('/contact/', methods={'POST'})
def truc():
    mail = 't.d@mail.fr'
    adr = '222 NickonNiki'
    return f'{mail}, {adr} {request.path} {request.method} {dir(request)} {request.get_json}'

@app.route('/papy/', methods={'GET'})
def papy():
    return render_template('papy.html')

@app.route('/api/', methods={'POST'})
def api():
    # la recherche doit s'effectuer en appuyant sur entrée, non sur un bouton
    user_input = request.data.decode('utf-8')

    lat, lng, formatted_address = googlemaps.init(normalize(user_input))
    print(lat, lng)
    if not lat:
        return jsonify({'hum':1})

    wiki_info = wikipedia.Wiki().req(lat, lng)
    print(wiki_info.url)

    return jsonify({
        'lat': lat,
        'lng': lng,
        'formatted_address': formatted_address,
        'wiki_url': wiki_info.url
        }) # + console.log

@app.errorhandler(404)
def page_404(error):
    return f"Page introuvable. ERROR 404 by me", 404

@app.route('/animaux/')
def animaux():
    return render_template('animaux.html')

if __name__ == "__main__":
    app.run()
