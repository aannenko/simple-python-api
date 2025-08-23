from flask import Flask

from database import db
from routes import sightseeing_routes


db.create()

app = Flask(__name__)
sightseeing_routes.register(app)
