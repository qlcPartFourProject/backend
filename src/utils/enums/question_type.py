from enum import Enum

class QuestionType(Enum):
    FUNCTION_NAME = 'FunctionName'
    FUNCTION_PARAMETER_LIST = 'FunctionParameterList'
    LINE_AT_END_OF_LOOP = 'LineAtEndOfLoop'