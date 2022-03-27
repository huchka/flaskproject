import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

# default is FLASK_ENV=development
app.config.from_object('flaskr.config')

db = SQLAlchemy(app)
ma = Marshmallow(app)

migrate = Migrate(app, db)

import flaskr.views
