from .RoleResource import RolesResource

def right_routes(api):
    api.add_resource(RolesResource, '/api/roles')