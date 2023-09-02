from flask_restful import Resource
from flask import make_response, request

from src.dtos.quiz.create_submission import CreateSubmission
from src.services.survey_service import add_survey_results

class SurveyController(Resource):
    def post(self, id: str):
        create_submission = CreateSubmission(id)
        
        for answer_tuple in enumerate(request.get_json().get('answers')):
            answer = answer_tuple[1]
            print(answer)
            create_submission.set_question_answer(answer.get('questionId'), answer.get('choiceIds'))

        res = add_survey_results(create_submission) # returns submission id

        return make_response(res, 200)