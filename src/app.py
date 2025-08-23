import inject
from flask import Flask

from database import db
from dependencyinjection import di
from routes import sightseeing_routes

inject.configure(di.configure_inject)

db.create()

app = Flask(__name__)
sightseeing_routes.register(app)
