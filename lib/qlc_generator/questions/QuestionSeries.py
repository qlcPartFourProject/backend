import re
from lib.qlc_generator.questions.Question import Question

class QuestionSeries:
    def __init__(self, questions: list[Question]):
        self.questions = questions

    def start(self):
        for q in self.questions:
            q.ask()

    def get_score(self):
        score = 0
        for q in self.questions:
            if q.answered_correctly():
                score += 1
                
        return score

    def json(self):
        questions_json = []
        for idx, q in enumerate(self.questions):
            q_json = q.json()
            q_json['_id'] = idx # set question id

            questions_json.append(q_json)

        return {
            '_id': 0,
            'programId': 0,
            'questions': questions_json
        }