from .users import user_routes
from .blogposts import blogpost_routes
from .rights import right_routes

def create_routes(api):
    user_routes(api)
    blogpost_routes(api)
    right_routes(api)