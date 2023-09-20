from questions.Question import Question
from questions.FunctionParameterListQuestion import FunctionParameterListQuestion
import ast
from util.AstUtil import AstUtil
from util.Analyzer import Analyzer
import os
from pathlib import Path
import pytest
from unittest import mock
import random
from answers.Answer import Answer

class TestFunctionParameterListQuestion: 
   @pytest.fixture
   def setup_before_test(self):
      path = Path(os.path.abspath(__file__)).parent.absolute()

      yield path

   def generate_testing_ast(self, code_filepath):
      with open(code_filepath, "r") as source:
        tree = ast.parse(source.read())

      return tree
   
   def generate_ast_util(self, tree):
      analyzer = Analyzer()
      analyzer.visit(tree)

      return analyzer.astUtil
   
   def test_selects_valid_node(self, setup_before_test):
      path = setup_before_test
      tree = self.generate_testing_ast(os.path.join(path, "test_source_code/single_function.py"))
      
      ast_util = AstUtil()
      ast_util.functionDefNodes.append(tree.body[0])
      
      question = FunctionParameterListQuestion(ast_util)
      question.select_node()

      assert question.node == tree.body[0]

   def test_generates_correct_answer(self, setup_before_test):
      path = setup_before_test
      tree = self.generate_testing_ast(os.path.join(path, "test_source_code/single_function.py"))

      question = FunctionParameterListQuestion(AstUtil())
      question.node = tree.body[0]
      question.generate_correct_answer()
      actualCorrectAnswer = question.get_correct_answer()
      
      assert actualCorrectAnswer.get_answer_value() == "['parameter_1']"

   def test_selects_function_name_as_distractor(self, setup_before_test):
      path = setup_before_test
      tree = self.generate_testing_ast(os.path.join(path, "test_source_code/single_function.py"))
      ast_util = self.generate_ast_util(tree)

      question = FunctionParameterListQuestion(ast_util)
      question.node = tree.body[0] # function_1

      question.generate_distractors()

      actual_distractor_pool = question.get_distractor_pool()

      assert Answer('foo', False) in actual_distractor_pool
      assert len(actual_distractor_pool) == 1

   def test_selects_other_functions_parameter_lists_as_distractors(self, setup_before_test):
      path = setup_before_test
      tree = self.generate_testing_ast(os.path.join(path, "test_source_code/multiple_functions.py"))
      ast_util = self.generate_ast_util(tree)

      question = FunctionParameterListQuestion(ast_util)
      question.node = tree.body[0] # function_1

      question.generate_distractors()

      actual_distractor_pool = question.get_distractor_pool()
      
      assert Answer('function_1', False) in actual_distractor_pool
      assert Answer("['function_2_param']", False) in actual_distractor_pool
      assert Answer("['function_3_param']", False) in actual_distractor_pool
      assert Answer("['function_4_param']", False) in actual_distractor_pool
      assert len(actual_distractor_pool) == 4

   def test_ignores_invalid_param_list_functions(self, setup_before_test):
      path = setup_before_test
      tree = self.generate_testing_ast(os.path.join(path, "test_source_code/multiple_functions_invalid_param_lists.py"))
      ast_util = self.generate_ast_util(tree)

      question = FunctionParameterListQuestion(ast_util)
      question.node = tree.body[0] # function_1

      question.generate_distractors()

      actual_distractor_pool = question.get_distractor_pool()

      assert Answer("['param']", False) not in actual_distractor_pool
      assert Answer("[]", False) not in actual_distractor_pool
      assert Answer('function_1', False) in actual_distractor_pool
      assert len(actual_distractor_pool) == 1

   def test_selects_function_variables_as_distractors(self, setup_before_test):
      path = setup_before_test
      tree = self.generate_testing_ast(os.path.join(path, "test_source_code/function_with_variables.py"))
      ast_util = self.generate_ast_util(tree)

      question = FunctionParameterListQuestion(ast_util)
      question.node = tree.body[0] # function_1

      question.generate_distractors()

      actual_distractor_pool = question.get_distractor_pool()

      assert Answer("['var_1', 'var_2', 'var_3']", False) in actual_distractor_pool
      assert Answer('function_1', False) in actual_distractor_pool
      assert len(actual_distractor_pool) == 2

   def test_selects_all_valid_distractors(self, setup_before_test):
      path = setup_before_test
      tree = self.generate_testing_ast(os.path.join(path, "test_source_code/complex_test_case.py"))
      ast_util = self.generate_ast_util(tree)

      question = FunctionParameterListQuestion(ast_util)
      question.node = tree.body[0] # function_1

      question.generate_distractors()

      actual_distractor_pool = question.get_distractor_pool()

      assert Answer("['param_1_function_2', 'param_2_function_2']", False) in actual_distractor_pool
      assert Answer("['var_1_function_1', 'var_2_function_1']", False) in actual_distractor_pool
      assert Answer('function_1', False) in actual_distractor_pool
      assert len(actual_distractor_pool) == 3

   def test_creates_question_text(self, setup_before_test):
      path = setup_before_test
      tree = self.generate_testing_ast(os.path.join(path, "test_source_code/single_function.py"))

      question = FunctionParameterListQuestion(AstUtil())
      question.node = tree.body[0]
      question.create_question_text()

      assert question.text == "Which are the parameters of the function on line 1?"