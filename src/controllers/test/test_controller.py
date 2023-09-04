from flask_restful import Resource
from flask import make_response
from src.utils.cors.response import _corsify_actual_response

class TestController(Resource):
    def get(self):
        return _corsify_actual_response(make_response({ 'status': 'Server is running... --test' }, 200))
    
