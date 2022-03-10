from flask import Flask
from .config import app_config
from .models import db, bcrypt, ma
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from .resources.UserResource import UsersListResource
from .resources.BlogPostResource import BlogPostsListResource
from .resources.AuthResource import LoginResource, RegisterResource


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

  api.add_resource(UsersListResource, '/users')
  api.add_resource(BlogPostsListResource, '/blogposts')
  api.add_resource(LoginResource, '/login')
  api.add_resource(RegisterResource, '/register')


  return app