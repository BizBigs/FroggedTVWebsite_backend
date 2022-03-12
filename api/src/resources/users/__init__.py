from .UserResource import UsersListResource
from .AuthResource import LoginResource, RegisterResource

def user_routes(api):
    api.add_resource(UsersListResource, '/users')
    api.add_resource(LoginResource, '/login')
    api.add_resource(RegisterResource, '/register')