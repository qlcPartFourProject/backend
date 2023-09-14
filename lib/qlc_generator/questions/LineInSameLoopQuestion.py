import random
from lib.qlc_generator.questions.Question import Question
from lib.qlc_generator.answers.Answer import Answer
from lib.qlc_generator.answers.AnswerOptions import AnswerOptions
from lib.qlc_generator.util.AstUtil import AstUtil
from ast_decompiler import decompile
import ast

class LineInSameLoopQuestion(Question):
    def __init__(self, astUtil: AstUtil):
        
        super().__init__(astUtil)
        self.selected_line = ast.AST()

    def select_node(self):
        valid_loops = []
        for loop in self.astUtil.getForNodes():
            # only select loops with at least 2 lines
            if len(AstUtil.get_lines(loop)) >= 2:
                valid_loops.append(loop)

        for loop in self.astUtil.getWhileNodes():
            # only select loops with at least 2 lines
            if len(AstUtil.get_lines(loop)) >= 2:
                valid_loops.append(loop)

        # loop to quiz on
        self.node = random.choice(valid_loops)

    def generate_correct_answer(self):
        line = random.choice(AstUtil.get_lines(self.node))
        self.selected_line = line
        line_text = decompile(line).partition("\n")[0]
        self.correct_answer = Answer(line_text, True)
    
    def generate_distractors(self):
        distractorPool = []

        # get text of all lines inside loop to handel the case of duplicated
        # code inside and outside the loop
        lines_inside_loop_text = []
        for line in AstUtil.get_lines(self.node):
            lines_inside_loop_text.append(decompile(line).partition("\n")[0])

        # lines outside the loop
        function_def_nodes = self.astUtil.getFunctionDefNodes()
        for func in function_def_nodes:
            for line in AstUtil.get_lines(func):
                lineText = decompile(line).partition("\n")[0]
                if lineText not in lines_inside_loop_text:
                    distractorPool.append(Answer(lineText, False))

        self.distractor_pool = distractorPool
    
    def create_question_text(self):
        valid_lines = [x for x in AstUtil.get_lines(self.node) if x != self.selected_line]
        question_line = random.choice(valid_lines)
        question_line_number = str(question_line.lineno)
        question_line_text = decompile(question_line).partition("\n")[0]
        self.text = "The following line of code on line " + question_line_number + " is contained in a loop:\n\n " + question_line_text + ".\n\n Which other line is contained inside the same loop?"