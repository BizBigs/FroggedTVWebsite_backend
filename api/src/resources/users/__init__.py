from .UserResource import UsersListResource
from .AuthResource import LoginResource, RegisterResource

def user_routes(api):
    api.add_resource(UsersListResource, '/api/users')
    api.add_resource(LoginResource, '/api/login')
    api.add_resource(RegisterResource, '/api/register')