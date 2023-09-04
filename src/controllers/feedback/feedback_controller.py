from flask_restful import Resource
from flask import make_response, request

from src.dtos.feedback.feedback_submission import FeedbackSubmission
from src.services.feedback_service import add_feedback_results

class FeedbackController(Resource):
    def post(self, id: str):
        feedback_submission = FeedbackSubmission(id, request.get_json().get('text'))

        res = add_feedback_results(feedback_submission) # returns submission id

        return make_response(res, 200)