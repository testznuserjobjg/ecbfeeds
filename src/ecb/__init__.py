# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Default config name
config_name = 'DevelopmentConfig'


# import  feedparser
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('instance.config.' + config_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .routes import routes
from flask import Blueprint
import flask_restful as restful
from .validators import security


bp = Blueprint('', __name__, static_folder='static')
api = restful.Api(bp, catch_all_404s=True)
for route in routes:
    api.add_resource(route.pop('resource'), *route.pop('urls'), **route)

app.register_blueprint(bp)
