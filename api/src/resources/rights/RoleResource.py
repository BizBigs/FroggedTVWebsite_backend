from flask_restful import Resource
from ...models.RoleModel import RoleModel, roles_schema, role_schema
from flask import Response, request, jsonify, make_response, current_app as app

class RolesResource(Resource):
    def get(self):
        roles = RoleModel.query.all()
        return roles_schema.dump(roles)

    def post(self):
        body = request.get_json()
        if not body or not body.get('role_name'):
            return make_response(
                        'Wrong data format.',
                        401,
                        {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
                    )

        role = RoleModel.query\
                .filter_by(role_name = body.get('role_name'))\
                .first()

        if not role:
            role = RoleModel(
                role_name = body.get('role_name')
            )
            try:
                result = role_schema.load(body)
            except ValidationError as err:
                return err.messages, 422

            RoleModel.addRole(role)
            return make_response('Successfully registered.', 201)
