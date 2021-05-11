from flask import Flask, request, make_response, render_template, jsonify
import requests
import json

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "Salut Thibault"

@app.route('/hello/')
def hello():
    return "Ho great !"

@app.route('/contact/', methods={'GET', 'POST'})
# il est possible de générer deux routes distinctes :
# @app.route('/contact/', methods={'GET'})
# @app.route('/contact/', methods={'POST'})
def truc():
    mail = 't.d@mail.fr'
    adr = '222 NickonNiki'
    return f'{mail}, {adr} {request.path} {request.method} {dir(request)} {request.get_json}'

@app.route('/recup/')
def recup():
    allo = requests.get('http://127.0.0.1:5000/papy/')
    print(allo.content.decode('utf-8'))
    return render_template('papy.html')

@app.route('/cupcake/')
def cupcake():
    return render_template('cupcake.html')

@app.route('/papy/', methods={'GET'})
def papy():
    return render_template('papy.html')

@app.route('/api/', methods={'POST'})
def api():
    #allo = requests.get('http://127.0.0.1:5000/papy/api/')
    #if allo.status_code == 200:
    #    print(dir(allo))
    #    print(allo.content)
    #    return jsonify({'blabla':1})
    print(request.data.decode('utf-8'))
    return jsonify({'hum':1})

@app.errorhandler(404)
def page_404(error):
    return f"Page introuvable. ERROR 404 by me", 404

@app.route('/accueil/')
def accueil():
    return render_template('truc.html')

@app.route('/animaux/')
def animaux():
    return render_template('animaux.html')

if __name__ == "__main__":
    app.run()
