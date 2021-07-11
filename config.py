
class Google:
    GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json?"

    # See https://developers.google.com/maps/documentation/javascript/geocoding#GeocodingStatusCodes
    class Status(str):
        OK = 'OK'
        ZERO_RESULTS = 'ZERO_RESULTS'
        OVER_QUERY_LIMIT = 'OVER_QUERY_LIMIT'
        REQUEST_DENIED = 'REQUEST_DENIED'
        INVALID_REQUEST = 'INVALID_REQUEST'
        UNKNOWN_ERROR = 'UNKNOWN_ERROR'
        ERROR = 'ERROR'

        @property
        def is_ok(self):
            return self == self.__class__.OK

        @property
        def is_error_from_server(self):
            return self in (self.__class__.UNKNOWN_ERROR, self.__class__.ERROR)

        @property
        def is_error_from_user(self):
            return not self.is_ok and not self.is_error_from_server

class Wiki:
    DEFAULT_URL = "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal"
    URL = "https://fr.wikipedia.org/w/api.php"
    SEARCH_URL = "https://fr.wikipedia.org/wiki?"

class Return:
    SERVER_ERROR = -3
    USER_ERROR = -2
    URL_ERROR = -1
    DEFAULT_ERROR = 0
    NO_RETURN = 1
    RETURN_OK = 2

