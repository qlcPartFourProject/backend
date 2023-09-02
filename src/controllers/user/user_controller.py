from flask_restful import Resource
from flask import jsonify, make_response, abort
from src.services.user_service import get_user

class UserController(Resource):
    def get(self, id: str):
        user = get_user(id)
        if user.exists:
            return make_response(user.to_dict(), 200)
        abort(404)