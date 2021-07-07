from flask import Flask
from config import DEV

app = Flask(__name__)
app.debug = DEV == 'TEST'

from gdpy import views
