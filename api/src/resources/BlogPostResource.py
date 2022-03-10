from flask_restful import Resource
from ..common.authentication.TokenManager import token_required
from ..models.BlogPostModel import BlogPostModel, blogposts_schema

class BlogPostsListResource(Resource):
    @token_required
    def get(current_user, self):
        blogposts = BlogPostModel.query.all()
        return blogposts_schema.dump(blogposts)

    #def post(self):
    #    new_post = Post(
    #        title=request.json['title'],
    #        content=request.json['content']
    #    )
    #    db.session.add(new_post)
    #    db.session.commit()
    #    return post_schema.dump(new_post)