from src.models.quiz import Choice, Question, Quiz
from src.utils.enums.question_type import QuestionType

def all_quizzes():
    return [
        Quiz(
            _id = 0,
            program_id = 0,
            questions = [
                Question(
                    _id = 0,
                    type = QuestionType.FUNCTION_NAME,
                    text = 'What is the name of the function on line <line no testing>?',
                    choices = [
                        Choice(_id = 0, text = 'f0', is_correct = True),
                        Choice(_id = 1, text = 'f1', is_correct = False),
                        Choice(_id = 2, text = 'f2', is_correct = False),
                        Choice(_id = 3, text = 'f3', is_correct = False),
                    ]
                ),
                Question(
                    _id = 1,
                    type = QuestionType.FUNCTION_PARAMETER_LIST,
                    text = 'Which are the parameter names of the function on line <line no>?',
                    choices = [
                        Choice(_id = 0, text = 'p4, p5', is_correct = False),
                        Choice(_id = 1, text = 'p0, p3, p5', is_correct = False),
                        Choice(_id = 2, text = 'p0, p1, p2, p3', is_correct = True),
                        Choice(_id = 3, text = 'The function has no parameters', is_correct = False),
                    ]
                ),
                Question(
                    _id = 2,
                    type = QuestionType.LINE_AT_END_OF_LOOP,
                    text = 'A program loop starts on line <line no>. What is the last line inside it?',
                    choices = [
                        Choice(_id = 0, text = 'print(\'Calculation complete\')', is_correct = False),
                        Choice(_id = 1, text = 'i++', is_correct = False),
                        Choice(_id = 2, text = 'sum = num1 + num2', is_correct = True),
                        Choice(_id = 3, text = 'None of the above', is_correct = False),
                    ]
                ),
                Question(
                    _id = 3,
                    type = QuestionType.FUNCTION_NAME,
                    text = 'What is the name of the function on line <line no>?',
                    choices = [
                        Choice(_id = 0, text = 'f0', is_correct = False),
                        Choice(_id = 1, text = 'f1', is_correct = False),
                        Choice(_id = 2, text = 'f2', is_correct = True),
                        Choice(_id = 3, text = 'f3', is_correct = False),
                    ]
                ),
                Question(
                    _id = 4,
                    type = QuestionType.FUNCTION_PARAMETER_LIST,
                    text = 'Which are the parameter names of the function on line <line no>?',
                    choices = [
                        Choice(_id = 0, text = 'f1, p1, v1', is_correct = False),
                        Choice(_id = 1, text = 'p2, p4, p6', is_correct = True),
                        Choice(_id = 2, text = 'f1, f2', is_correct = False),
                        Choice(_id = 3, text = 'None of the above', is_correct = False),
                    ]
                ),
            ]
        )
    ]