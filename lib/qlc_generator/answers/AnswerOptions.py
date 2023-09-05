import string
from lib.qlc_generator.answers.Answer import Answer

class AnswerOptions: 
    def __init__(self, answers: list[Answer]):
        self.answersLookup = {}
        for i in range(len(answers)):
            self.answersLookup[chr(ord('A') + i)] = answers[i]
    
    def is_correct_answer(self, code: string) -> bool:
        return self.answersLookup[code].isCorrect
    
    def __str__(self):
        str = ""
        options = list(self.answersLookup.keys())
        for i, optionCode in enumerate(options):
            str += optionCode + ") " + self.answersLookup[optionCode].__str__() 
            if i < len(options)-1:
                str += "\n" 

        return str
    
    def json(self):
        choices = []
        options = list(self.answersLookup.keys())
        for optionCode in options:
            choice = self.answersLookup[optionCode]
            choices.append({
                'text': choice.__str__(),
                'isCorrect': choice.isCorrect
            })

        return choices