import string
import random
import re
from lib.qlc_generator.answers.AnswerOptions import AnswerOptions
from abc import ABC, abstractmethod
from lib.qlc_generator.util.AstUtil import AstUtil
import ast
from lib.qlc_generator.answers.Answer import Answer

class Question(ABC): 
    def __init__(self, astUtil: AstUtil):
        self.astUtil = astUtil
        self.node = ast.AST()
        self.text = ''
        self.answer_options = AnswerOptions([])
        self.selected_answer: string = None
        self.correct_answer: Answer = None
        self.distractor_pool: list(Answer) = []

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
    
    @abstractmethod
    def select_node(self):
        pass
    
    @abstractmethod
    def generate_correct_answer(self):
        pass
    
    @abstractmethod
    def generate_distractors(self):
        pass
    
    @abstractmethod
    def create_question_text(self):
        pass
    
    def select_distractors(self):
        random.shuffle(self.distractor_pool)
        return self.distractor_pool[:3]
    
    def create_answer_options(self):
        answers = self.select_distractors()
        answers.append(self.correct_answer)
        random.shuffle(answers)
        self.answer_options = AnswerOptions(answers)

    def get_correct_answer(self):
        return self.correct_answer
    
    def get_distractor_pool(self):
        return self.distractor_pool
    
    def json(self):
        # get question type
        class_name = self.__class__.__name__
        res = re.findall('[A-Z][^A-Z]*', class_name) # removes 'Question' suffix
        type = ''.join(res[:len(res)-1])

        return {
            'text': self.text,
            'choices': self.answer_options.json(),
            'type': type
        }