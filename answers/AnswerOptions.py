import string
from answers.Answer import Answer

class AnswerOptions: 
    def __init__(self, answers: list[Answer]):
        self.answersLookup = {
            "A": answers[0],
            "B": answers[1],
            "C": answers[2],
            "D": answers[3],
        }
    
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