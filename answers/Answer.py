class Answer:
    def __init__(self, text, isCorrect):
        self.text = text
        self.isCorrect = isCorrect

    def __str__(self):
        return self.text