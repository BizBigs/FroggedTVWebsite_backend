from .BlogPostResource import BlogPostsListResource

def blogpost_routes(api):
    api.add_resource(BlogPostsListResource, '/blogposts')