from answers.AnswerOptions import AnswerOptions
from answers.Answer import Answer
from questions.Question import Question
from util.AstUtil import AstUtil
import io
import ast

# implement abstract methods of question class 
# so non-abstract methods can be tested
class ConcreteQuestion(Question):
    def select_node(self):
        pass
    
    def generate_correct_answer(self):
        pass
    
    def generate_distractors(self):
        pass
    
    def create_question_text(self):
        pass
    
class TestQuestion: 
    correctAnswer = Answer('correct answer', True)
    wrongAnswer1 = Answer('wrong answer 1', False)
    wrongAnswer2 = Answer('wrong answer 2', False)
    wrongAnswer3 = Answer('wrong answer 3', False)
    answers = AnswerOptions([correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3])
    question = ConcreteQuestion(AstUtil())
    question.answer_options = answers

    def test_question_correct_answer(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO('A'))
        self.question.ask()
        assert self.question.answered_correctly()

    def test_question_wrong_answer(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO('B'))
        self.question.ask()
        assert not self.question.answered_correctly()


