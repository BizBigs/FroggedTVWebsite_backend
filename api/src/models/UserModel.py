import datetime
from . import db, ma
from .BlogPostModel import BlogPostSchema
from .ProfileModel import ProfileSchema

class UserModel(db.Model):
  """
  User Model
  """

  # table name
  __tablename__ = 'ftv_user'

  id_user = db.Column(db.Integer, primary_key=True)
  public_id = db.Column(db.String(50), unique = True)
  nickname = db.Column(db.String(20), nullable=False, unique=True)
  email = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.String(128), nullable=True)
  created_at = db.Column(db.DateTime)
  last_modified = db.Column(db.DateTime)
  blogposts = db.relationship('BlogPostModel', backref='ftv_user', lazy=True)
  profiles = db.relationship('ProfileModel', backref='ftv_user', lazy=True)

  def addUser(newUser):
    # insert user
    db.session.add(newUser)
    db.session.commit()

  def __repr__(self):
    return '<User Id: %s>' % self.id_user

class UserSchema(ma.Schema):
  class Meta:
    fields = ("id_user", "public_id", "nickname", "email", "password", "created_at", "last_modified")

user_schema = UserSchema()
users_schema = UserSchema(many=True)