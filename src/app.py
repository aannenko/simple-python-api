from flask import Flask

from routes import sightseeing_routes


app = Flask(__name__)
sightseeing_routes.register(app)
