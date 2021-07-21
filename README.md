# GrandPy Project

GrandPy is a friendly old man who will give you the address of a place you are looking.
For while telling you a story about it.
If he knows your destination, he will give you a google map and a wikipedia link.


### Web part:
The application looks like a messaging application :
you write your question in the box provided for this purpose then press the 'Envoyer' button.
Please note, GrandPy is of French origin, his answers will also be in French.
GrandPy will answer you very quickly.


### Server part:
The user query is analysed and fragmented.
A request to GoogleMaps API is sent. In return : the place coordinates.
With coordinates, a request to MediaWiki API is sent. In return : the wikipedia page content.
With this informations, GrandPy generate an atypical answer.


#### Languages:
* Python3.8
* HTML5
* CSS3
* Javascript

#### Tools:
* Flask Framework (with fetch method)
* Bootstrap (for design)

#### API:
* GoogleMaps 
* MediaWiki


### Prerequisites:
* Python3
* pipenv

## Program flow: local use
1. Download this app :
```
git clone https://github.com/RiwsPy/OC_P7.git
```

2. Open the OC_P7 folder

3. Rename _.env.sample_ in _.env_

4. Write your own Google Key:
GOOGLE_MAPS_KEY= your_key

5. Install the virtual virtual environment
```
    pipenv install
    pipenv shell
```

6. Start the application
```
    python main.py
```

By default, your application is available here:
http://127.0.0.1:5000/


## Program flow: online use
This application is available in Heroku:
https://grandpy-in-the-sky.herokuapp.com/


### Architecture:
.env
main.py
- gdpy/
    - gdpy_app/
        - api/
            - googlemaps.py
            - wikipedia.py
        - tests/
            - test_*.py
        - config.py
    - website/
        - static/
            - css/
            - fonts/
            - img/
            - js/
        - templates/
            - index.html
        - views.py
