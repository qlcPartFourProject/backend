from questions.Question import Question

class QuestionGenerator():
    def __init__(self, stats):
        self.stats = stats

    def generate_question(self, question_type: Question):
        return question_type(self.stats)
