import random
from lib.qlc_generator.questions.Question import Question
from lib.qlc_generator.answers.Answer import Answer
from lib.qlc_generator.answers.AnswerOptions import AnswerOptions
from lib.qlc_generator.util.AstUtil import AstUtil
from ast_decompiler import decompile

class LineAtEndOfLoopQuestion(Question):
    def __init__(self, astUtil: AstUtil):

        super().__init__(astUtil)

    def select_node(self):
        # filter out loops that have another node with a body (for, if) as the last line
        valid_loops = []
        for loop in self.astUtil.getForNodes():
            if not hasattr(AstUtil.get_lines(loop)[-1], "body"):
                valid_loops.append(loop)

        for loop in self.astUtil.getWhileNodes():
            if not hasattr(AstUtil.get_lines(loop)[-1], "body"):
                valid_loops.append(loop)

        # loop to quiz on
        self.node = random.choice(valid_loops)

    def generate_correct_answer(self):
        line_text = decompile(AstUtil.get_lines(self.node)[-1]).partition("\n")[0]
        self.correct_answer = Answer(line_text, True)
    
    def generate_distractors(self):
        distractorPool = []

        # every line in the loop, except the last one
        for line in AstUtil.get_lines(self.node)[:-1]:
            lineText = decompile(line).partition("\n")[0]
            distractorPool.append(Answer(lineText, False))

        parent = self.node.parent
        for line in AstUtil.get_lines(parent):
            lineText = decompile(line).partition("\n")[0]
            distractorPool.append(Answer(lineText, False))

        self.distractor_pool = distractorPool
    
    def create_question_text(self):
        self.text = "A program loop starts on line " + str(self.node.lineno) + ". What is the last line inside it?"