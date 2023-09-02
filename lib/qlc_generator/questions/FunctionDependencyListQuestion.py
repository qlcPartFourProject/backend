import random
from lib.qlc_generator.questions.Question import Question
from lib.qlc_generator.answers.Answer import Answer
from lib.qlc_generator.answers.AnswerOptions import AnswerOptions
from lib.qlc_generator.util.AstUtil import AstUtil

class FunctionDependencyListQuestion(Question):
    def __init__(self, astUtil: AstUtil):

        super().__init__(astUtil)

    def select_node(self):
      valid_functions = []
      for func in self.astUtil.getFunctionDefNodes():
            defined_function_calls = AstUtil.get_user_defined_function_call_list(func, self.astUtil)
            if defined_function_calls:
                valid_functions.append(func)

      self.node = random.choice(valid_functions)
    
    def generate_correct_answer(self):
        defined_function_calls = AstUtil.get_user_defined_function_call_list(self.node, self.astUtil)

        self.correct_answer = Answer(defined_function_calls, True)

    def generate_distractors(self):
        distractor_pool = []
        if AstUtil.get_parameter_list(self.node):
            distractor_pool.append(Answer(AstUtil.get_parameter_list(self.node), False))

        if AstUtil.get_variable_list(self.node):
            distractor_pool.append(Answer(AstUtil.get_variable_list(self.node), False))

        for func in self.astUtil.getFunctionDefNodes():
            defined_function_calls = AstUtil.get_user_defined_function_call_list(func, self.astUtil)
            if defined_function_calls:
              if defined_function_calls != self.correct_answer.get_answer_value():
                  distractor_pool.append(Answer(defined_function_calls, False))

        self.distractor_pool = distractor_pool
    
    def create_question_text(self):
        self.text =  "Which functions does function " + str(self.node.name) + " depend on?"