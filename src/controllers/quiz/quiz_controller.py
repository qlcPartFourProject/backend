from flask_restful import Resource
from flask import make_response, request

from src.services.quiz_service import get_quiz_by_id, create_quiz_submission
from src.dtos.quiz.create_submission import CreateSubmission

class QuizController(Resource):
    def get(self, id: str):
        data = get_quiz_by_id(id)

        return make_response(data, 200)
    
    def post(self, id: str):
        create_submission = CreateSubmission(id)
        
        for answer_tuple in enumerate(request.get_json().get('answers')):
            answer = answer_tuple[1]
            print(answer)
            create_submission.set_question_answer(answer.get('questionId'), answer.get('choiceIds'))

        res = create_quiz_submission(create_submission) # returns submission id

        return make_response(res, 200)