bind = "127.0.0.1:5000"

PAPY_URL = 'http://127.0.0.1:5000/api/'
GOOGLE_MAPS_KEY= "AIzaSyDICnA0VqhMKNXJkwbZuWP26CMAedvYWVs"

class Google:
    GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json?"
    STATUS_OK = 'OK'
    STATUS_NO_RESULT = 'NO_RESULT'

class Wiki:
    DEFAULT_URL = "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal"
    URL = "https://fr.wikipedia.org/w/api.php"
    SEARCH_URL = "https://fr.wikipedia.org/wiki?"

class Return:
    UNKNOWN_EVENT = -4
    WIKI_ERROR = -3
    COORD_ERROR = -2
    URL_ERROR = -1
    DEFAULT_ERROR = 0
    NO_RETURN = 1
    RETURN_OK = 2

