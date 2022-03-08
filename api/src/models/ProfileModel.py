import datetime
from . import db, ma

class ProfileModel(db.Model):
  """
  User Model
  """

  # table name
  __tablename__ = 'ftv_profile'

  id_profile = db.Column(db.Integer, primary_key=True)
  mmr = db.Column(db.SmallInteger)
  steam_id = db.Column(db.String(20), unique=True)
  created_at = db.Column(db.DateTime)
  last_modified = db.Column(db.DateTime)
  user_id = db.Column(db.Integer, db.ForeignKey('ftv_user.id_user'), nullable=False)

  def __repr__(self):
    return '<Profile Id: %s>' % self.id_profile

class ProfileSchema(ma.Schema):
  class Meta:
    fields = ("id_profile", "mmr", "steam_id", "created_at", "last_modified", "user_id")

profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)