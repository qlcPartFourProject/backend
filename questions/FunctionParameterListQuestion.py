import random
from questions.Question import Question
from answers.Answer import Answer
from answers.AnswerOptions import AnswerOptions
from models.FunctionModel import FunctionModel

# NOTE: This assumes there is at least 1 function definition in the input Python program 
class FunctionParameterListQuestion(Question):
    def __init__(self, stats):
        # all function defs
        function_defs = stats["functionDef"].copy()
        random.shuffle(function_defs)
        function_defs = function_defs[:4]

        # set up answers
        answers = []

        # correct function
        correct_function = FunctionModel(function_defs[0])
        answers.append(Answer(correct_function.parameter_list().__str__(), True))

        # distractor functions
        for distractor_function_def in function_defs[1:4]:
            distractor_function = FunctionModel(distractor_function_def)
            answers.append(Answer(distractor_function.parameter_list().__str__(), False))

        # placeholders
        # TODO: add proper distractors (e.g. list of variable names)
        for i in range (0, 4-len(answers)):
            answers.append(Answer("<placeholder>", False))

        # set up choices for mcq
        random.shuffle(answers)

        super().__init__(
            "Which are the parameter names of the function on line " + str(function_defs[0].lineno) + "?", 
            AnswerOptions(answers)
        )
    
