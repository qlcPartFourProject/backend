from questions.Question import Question

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
