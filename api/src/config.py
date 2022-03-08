import os
from dotenv import dotenv_values

conf_env = dotenv_values(".env")

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = conf_env["JWT_SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = conf_env["DATABASE_URL"]

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = conf_env["DATABASE_URL"]
    JWT_SECRET_KEY = conf_env["JWT_SECRET_KEY"]

app_config = {
    'development': Development,
    'production': Production,
}