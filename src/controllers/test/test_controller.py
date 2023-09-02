from flask_restful import Resource
from flask import make_response, request

from src.dtos.quiz.create_submission import CreateSubmission
from src.services.survey_service import add_survey_results

class TestController(Resource):
    def get(self):
        return make_response({ 'status': 'Server is running...' }, 200)