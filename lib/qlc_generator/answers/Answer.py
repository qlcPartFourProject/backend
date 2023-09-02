class Answer:
    def __init__(self, answer_value, isCorrect):
        self.answer_value = answer_value
        self.isCorrect = isCorrect

    def get_answer_value(self):
        return self.answer_value

    def __str__(self):
        return str(self.answer_value)
    
    def __eq__(self, other):
        if isinstance(other, Answer):
            return self.answer_value == other.answer_value and self.isCorrect == other.isCorrect
        return False