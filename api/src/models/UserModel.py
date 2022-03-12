import datetime
from . import db, ma
from .BlogPostModel import BlogPostSchema
from .ProfileModel import ProfileSchema
from marshmallow import fields, validate
from sqlalchemy.sql import func

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
  created_at = db.Column(db.DateTime(timezone=True), nullable=False)
  last_modified = db.Column(db.DateTime(timezone=True))
  blogposts = db.relationship('BlogPostModel', backref='ftv_user', lazy=True)
  profiles = db.relationship('ProfileModel', backref='ftv_user', lazy=True)

  def addUser(newUser):
    # insert user
    db.session.add(newUser)
    db.session.commit()

  def __repr__(self):
    return '<User Id: %s>' % self.id_user

class UserSchema(ma.Schema):
  nickname = fields.String(required=True)
  email = fields.Email(required=True)
  class Meta:
    fields = ("nickname", "email", "created_at", "password", "last_modified")

user_schema = UserSchema()
users_schema = UserSchema(many=True)