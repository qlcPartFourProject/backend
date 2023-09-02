import string
from answers.AnswerOptions import AnswerOptions

class Question: 
    def __init__(self, text: string, answer_options: AnswerOptions):
        self.text: string = text
        self.answer_options: AnswerOptions = answer_options
        self.selected_answer: string = None

    def ask(self):
        # question and choices
        print(self.text)
        print(self.answer_options)

        # prompt user for an answer
        self.selected_answer = input()

        # feedback for user answer
        if self.answered_correctly():
            print("<correct answer>")
        else:
            print("<wrong answer>")

    def answered_correctly(self):
        if (self.selected_answer == None) or not (self.answer_options.is_correct_answer(self.selected_answer)):
            return False
        return True