import ast
from pathlib import Path
from configparser import ConfigParser

from questions.QuestionGenerator import QuestionGenerator
from questions.QuestionSeries import QuestionSeries
from questions.FunctionNameQuestion import FunctionNameQuestion 
from questions.FunctionParameterListQuestion import FunctionParameterListQuestion
from questions.LineAtEndOfLoopQuestion import LineAtEndOfLoopQuestion
from questions.DoesFunctionHaveDependenciesQuestion import DoesFunctionHaveDependenciesQuestion
from questions.NumberOfFunctionDependenciesQuestion import NumberOfFunctionDependenciesQuestion
from questions.FunctionDependencyListQuestion import FunctionDependencyListQuestion
from questions.IsFunctionRecursiveQuestion import IsFunctionRecursiveQuestion
from questions.NumberOfFunctionParametersQuestion import NumberOfFunctionParametersQuestion
from questions.FunctionVariableNameListQuestion import FunctionVariableNameListQuestion
from questions.NumberOfFunctionLoopsQuestion import NumberOfFunctionLoopsQuestion
from util.Analyzer import Analyzer

def main():
    # read config file
    config_file_path = Path(__file__).with_name('config.ini')
    config_object = ConfigParser()
    config_object.read(config_file_path)

    # get path to python file
    file_info = config_object["FILEINFO"]
    file_name = file_info["name"]
    python_file_path = Path(__file__).with_name(file_name)

    # read python file as AST
    with open(python_file_path, "r") as source:
        print(type(source))
        content = source.read()
        print(type(content))
        tree = ast.parse(content)

    # analyze AST contents
    analyzer = Analyzer()
    analyzer.visit(tree)

    # generate questions
    question_generator = QuestionGenerator(analyzer.astUtil)
    q1 = question_generator.generate_question(FunctionNameQuestion)
    q2 = question_generator.generate_question(FunctionParameterListQuestion)
    q3 = question_generator.generate_question(LineAtEndOfLoopQuestion)
    q4 = question_generator.generate_question(DoesFunctionHaveDependenciesQuestion)
    q5 = question_generator.generate_question(NumberOfFunctionDependenciesQuestion)
    q6 = question_generator.generate_question(FunctionDependencyListQuestion)
    q7 = question_generator.generate_question(IsFunctionRecursiveQuestion)
    q8 = question_generator.generate_question(NumberOfFunctionParametersQuestion)
    q9 = question_generator.generate_question(FunctionVariableNameListQuestion)
    q10 = question_generator.generate_question(NumberOfFunctionLoopsQuestion)

    # ask questions
    question_series = QuestionSeries([q1, q2, q3, q4, q5, q6, q7, q8, q9, q10])
    question_series.start()
    print(question_series.get_score())

if __name__ == "__main__":
    main()