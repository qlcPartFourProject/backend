import random
from questions.Question import Question
from answers.Answer import Answer
from answers.AnswerOptions import AnswerOptions
from models.FunctionModel import FunctionModel

class FunctionNameQuestion(Question):
    def __init__(self, stats):
        # function to quiz on
        f = random.choice(stats["functionDef"])	

        # add correct answer
        answers = [Answer(f.name, True)]

        # add distractors
        distractorPool = []
        for function in stats["functionDef"]:
            function_model = FunctionModel(function)
            for parameter in function_model.parameter_list():
                distractorPool.append(Answer(parameter, False))

        random.shuffle(distractorPool)
        answers +=  distractorPool[:3]

        # set up choices for mcq
        random.shuffle(answers)

        super().__init__(
            "What is the name of the function on line " + str(f.lineno) + "?", 
            AnswerOptions(answers)
        )