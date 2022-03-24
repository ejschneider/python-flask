from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt import jwt_required


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']) is None:
            user = UserModel(**data)
            user.save_to_db()
            return {"message": "User {} created successfully".format(data['username'])}, 201

        else:
            return {"message": "User {} already exists".format(data['username'])}, 400

    def delete(self):
        data = UserRegister.parser.parse_args()
        username = data['username']
        user = UserModel.find_by_username(username)
        if user:
            user.delete_from_db()
            return {'message': "User '{}' deleted".format(username)}, 200
        return {'message': "User {} not found".format(username)}, 400


class UserList(Resource):
    def get(self):
        return{'users': [user.json() for user in UserModel.query.all()]}

    @jwt_required()
    def delete(self):
        if UserModel.isEmpty():
            return {'message': 'no users fool'}
        else:
            for user in UserModel.query.all():
                user.delete_from_db()
            return {'message': 'All Users Deleted :('}
