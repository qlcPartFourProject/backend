import random
from lib.qlc_generator.questions.Question import Question
from lib.qlc_generator.answers.Answer import Answer
from lib.qlc_generator.answers.AnswerOptions import AnswerOptions
from lib.qlc_generator.util.AstUtil import AstUtil

class IsFunctionRecursiveQuestion(Question):
    def __init__(self, astUtil: AstUtil):

        super().__init__(astUtil)

    def select_node(self):
      self.node = random.choice(self.astUtil.getFunctionDefNodes())
    
    def generate_correct_answer(self):
        defined_function_calls = AstUtil.get_user_defined_function_call_list(self.node, self.astUtil)

        if self.node.name in defined_function_calls: 
            self.correct_answer = Answer('Yes', True)
        else: self.correct_answer = Answer('No', True)

    def generate_distractors(self):
        if self.correct_answer.get_answer_value() == 'Yes':
            self.distractor_pool = [Answer('No', False)]
        else: self.distractor_pool = [Answer('Yes', False)]
    
    def create_question_text(self):
        self.text =  "Is function " + str(self.node.name) + " recursive?"