from flask import Flask
import os
import setting

app = Flask(__name__)
app.debug = os.getenv('DEV_PHASE') == 'TEST'
print(os.getenv('DEV_PHASE'))
app.config.google_key = os.getenv('GOOGLE_MAPS_KEY')

from gdpy import views
