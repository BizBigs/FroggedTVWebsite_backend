from flask_restful import Resource
from flask import Response, request, jsonify, make_response, current_app as app
from ...models.UserModel import UserModel, user_schema
from  werkzeug.security import generate_password_hash, check_password_hash
from  werkzeug.exceptions import BadRequest
import uuid
from datetime import datetime, timedelta
import jwt
from marshmallow import ValidationError
from sqlalchemy import or_

class LoginResource(Resource):
    def post(self):
        body = request.get_json()
        if not body or not body.get('nickname') or not body.get('password'):
            return make_response(
                        'Could not verify',
                        401,
                        {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
                    )
        user = UserModel.query\
                .filter_by(nickname = body.get('nickname'))\
                .first()

        if not user:
            # returns 401 if user does not exist
            return make_response(
                'Could not verify',
                401,
                {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
            )

        if check_password_hash(user.password, body.get('password')):
                # generates the JWT Token
                token = jwt.encode({
                    'public_id': user.public_id,
                    'exp' : datetime.utcnow() + timedelta(minutes = 30)
                }, app.config['JWT_SECRET_KEY'], algorithm='HS256')

                return make_response(jsonify({'token' : token}), 201)

        return make_response(
                'Could not verify',
                403,
                {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
            )

class RegisterResource(Resource):
    def post(self):
        body = request.get_json()
        nickname, email = body.get('nickname'), body.get('email')
        password = body.get('password')

        user = UserModel.query\
                .filter(or_(UserModel.email == email, UserModel.nickname == nickname))\
                .first()
        if not user:
            # database ORM object
            user = UserModel(
                public_id = str(uuid.uuid4()),
                nickname = nickname,
                created_at = datetime.utcnow(),
                last_modified = datetime.utcnow(),
                email = email,
                password = generate_password_hash(password)
            )
            try:
                result = user_schema.load(body)
            except ValidationError as err:
                return err.messages, 422

            UserModel.addUser(user)
            return make_response('Successfully registered.', 201)
        else:
            # returns 202 if user already exists
            return make_response('User already exists. Please Log in.', 202)
