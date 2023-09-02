from questions.Question import Question

class Quiz:
    def __init__(self, program_id: str, questions: list[Question]):
        self.program_id = program_id
        self.questions = questions

    def json(self):
        questions_json = []
        for q in self.questions:
            q_json = q.json()
            questions_json.append(q_json)

        return {
            'programId': self.program_id,
            'questions': questions_json
        }