from flask_restful import Resource
from ..models.UserModel import UserModel, users_schema

class UsersListResource(Resource):
    def get(self):
        users = UserModel.query.all()
        return users_schema.dump(users)

    #def post(self):
    #    new_post = Post(
    #        title=request.json['title'],
    #        content=request.json['content']
    #    )
    #    db.session.add(new_post)
    #    db.session.commit()
    #    return post_schema.dump(new_post)