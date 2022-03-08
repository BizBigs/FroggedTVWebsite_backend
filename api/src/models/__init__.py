from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

# initialize our db
db = SQLAlchemy()

# password crypto
bcrypt = Bcrypt()

# init Marchmallow
ma = Marshmallow()