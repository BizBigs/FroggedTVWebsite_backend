from flask import Flask
from .config import app_config
from .models import db, bcrypt, ma
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .resources import create_routes
from flask_restful import Api, Resource

def create_app(env_name):
  """
  Create app
  """

  # app initiliazation
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])

  # initializing bcrypt
  bcrypt.init_app(app)
  db.init_app(app)
  ma.init_app(app)
  api = Api(app)

  create_routes(api)

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

  return app