import random
from questions.Question import Question
from answers.Answer import Answer
from answers.AnswerOptions import AnswerOptions
from util.AstUtil import AstUtil
from util.QuestionUtil import create_distractor_answer

class NumberOfFunctionVariablesQuestion(Question):
    def __init__(self, astUtil: AstUtil):
        super().__init__(astUtil)

    def select_node(self):
      self.node = random.choice(self.astUtil.getFunctionDefNodes())
    
    def generate_correct_answer(self):
        parameter_list = AstUtil.get_variable_list(self.node)

        self.correct_answer = Answer(len(parameter_list), True)

    def generate_distractors(self):
        correct_answer_number = int(self.correct_answer.get_answer_value())
        lower_bound = max(correct_answer_number - 3, 0)
        distractor_pool = list(range(lower_bound, correct_answer_number + 4))
        distractor_pool.remove(correct_answer_number)

        self.distractor_pool = list(map(create_distractor_answer, distractor_pool))

    def create_question_text(self):
        self.text =  "How many parameters does function " + str(self.node.name) + " have?"