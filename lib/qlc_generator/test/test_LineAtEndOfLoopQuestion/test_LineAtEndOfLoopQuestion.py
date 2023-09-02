from questions.Question import Question
from questions.LineAtEndOfLoopQuestion import LineAtEndOfLoopQuestion
import ast
from util.AstUtil import AstUtil
from util.Analyzer import Analyzer
import os
from pathlib import Path
import pytest
from unittest import mock
import random
from answers.Answer import Answer

class TestLineAtEndOfLoopQuestion: 
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
      tree = self.generate_testing_ast(os.path.join(path, "test_source_code/single_loop.py"))
      
      ast_util = AstUtil()
      ast_util.forNodes.append(tree.body[0].body[0])
      
      question = LineAtEndOfLoopQuestion(ast_util)
      question.select_node()

      assert question.node == tree.body[0].body[0]

   def test_generates_correct_answer(self, setup_before_test):
      path = setup_before_test
      tree = self.generate_testing_ast(os.path.join(path, "test_source_code/single_loop.py"))

      question = LineAtEndOfLoopQuestion(AstUtil())
      question.node = tree.body[0].body[0]
      question.generate_correct_answer()
      actualCorrectAnswer = question.get_correct_answer()
      
      assert actualCorrectAnswer.get_answer_value() == "pass"

   def test_selects_other_lines_as_distractors(self, setup_before_test):
      path = setup_before_test
      tree = self.generate_testing_ast(os.path.join(path, "test_source_code/loop_with_distractors.py"))
      ast_util = self.generate_ast_util(tree)

      question = LineAtEndOfLoopQuestion(ast_util)
      question.node = tree.body[0].body[1]

      question.generate_distractors()

      actual_distractor_pool = question.get_distractor_pool()

      assert Answer('var1 = 1', False) in actual_distractor_pool
      assert Answer('for i in range(10):', False) in actual_distractor_pool
      assert Answer('var2 = 2', False) in actual_distractor_pool
      assert len(actual_distractor_pool) == 3

   def test_creates_question_text(self, setup_before_test):
      path = setup_before_test
      tree = self.generate_testing_ast(os.path.join(path, "test_source_code/single_loop.py"))

      question = LineAtEndOfLoopQuestion(AstUtil())
      question.node = tree.body[0].body[0]
      question.create_question_text()

      assert question.text == "A program loop starts on line 2. What is the last line inside it?"