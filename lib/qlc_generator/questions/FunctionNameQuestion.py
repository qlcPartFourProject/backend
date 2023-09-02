import random
from lib.qlc_generator.questions.Question import Question
from lib.qlc_generator.answers.Answer import Answer
from lib.qlc_generator.util.AstUtil import AstUtil

class FunctionNameQuestion(Question):
    def __init__(self, astUtil: AstUtil):

        super().__init__(astUtil)

    def select_node(self):
      self.node = random.choice(self.astUtil.getFunctionDefNodes())
    
    def generate_correct_answer(self):
        self.correct_answer = Answer(self.node.name, True)
    
    def generate_distractors(self):
        distractorPool = []

        # parameter names and variable names associated with this function
        for parameter in AstUtil.get_parameter_list(self.node):
            distractorPool.append(Answer(parameter, False))
        for variable in AstUtil.get_variable_list(self.node):
            distractorPool.append(Answer(variable, False))

        # names of other functions
        for function in self.astUtil.getFunctionDefNodes():
            if function.name != self.node.name:
              distractorPool.append(Answer(function.name, False))

        self.distractor_pool = distractorPool
    
    def create_question_text(self):
        self.text =  "What is the name of the function on line " + str(self.node.lineno) + "?"
        