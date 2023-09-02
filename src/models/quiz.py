from flask import jsonify

class Choice:
    def __init__(self, _id: int, text: str, is_correct: bool):
        self._id = _id
        self.text = text
        self.is_correct = is_correct
    
    def json(self):
        return {
            '_id': self._id,
            'text': self.text,
            'isCorrect': self.is_correct
        }

class Question:
    def __init__(self, _id: int, type: str, text: str, choices: list[Choice]):
        self._id = _id
        self.type = type
        self.text = text
        self.choices = choices
    
    def json(self):
        choices_json = []
        for i in range(len(self.choices)):
            choices_json.append(self.choices[i].json())

        return {
            '_id': self._id,
            'type': self.type.value,
            'text': self.text,
            'choices': choices_json
        }

class Submission: 
    def __init__(self, _id: int):
        self._id = _id
        self.answers = []
    
    def set_question_answer(self, question_id: int, choice_ids: list[int]):
        question_answer = {
            'questionId': question_id,
            'choiceIds': choice_ids
        }
        self.answers.append(question_answer)

class Quiz:
    def __init__(self, _id: int, program_id: int, questions: list[Question]):
        self._id = _id
        self.program_id = program_id
        self.questions = questions
    
    def json(self):
        questions_json = []
        for i in range(len(self.questions)):
            questions_json.append(self.questions[i].json())

        return {
            '_id': self._id,
            'programId': self.program_id,
            'questions': questions_json
        }