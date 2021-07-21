from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.debug = os.getenv('DEV_PHASE') == 'TEST'
app.config.google_key = os.getenv('GOOGLE_MAPS_KEY')

from gdpy.website import views
