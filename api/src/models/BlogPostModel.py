from . import db, ma
import datetime

class BlogPostModel(db.Model):
  """
  Blogpost Model
  """

  __tablename__ = 'ftv_blog_post'

  id_blog_post = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128), nullable=False)
  content = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime)
  last_modified = db.Column(db.DateTime)
  author_id = db.Column(db.Integer, db.ForeignKey('ftv_user.id_user'), nullable=False)

  def __repr__(self):
    return '<id {}>'.format(self.id_blog_post)

class BlogPostSchema(ma.Schema):
  class Meta:
    fields = ("id_blog_post", "title", "content", "created_at", "last_modified", "author_id")

blogpost_schema = BlogPostSchema()
blogposts_schema = BlogPostSchema(many=True)