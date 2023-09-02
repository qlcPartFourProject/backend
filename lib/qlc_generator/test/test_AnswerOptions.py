from answers.AnswerOptions import AnswerOptions
from answers.Answer import Answer
import ast

class TestAnswerOptions: 
    correctAnswer = Answer('correct answer', True)
    wrongAnswer1 = Answer('wrong answer 1', False)
    wrongAnswer2 = Answer('wrong answer 2', False)
    wrongAnswer3 = Answer('wrong answer 3', False)
    answers = AnswerOptions([correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3])

    def test_question_correct_answer(self):
        assert self.answers.is_correct_answer("A") == True

    def test_question_wrong_answer(self):
        assert self.answers.is_correct_answer("B") == False
        assert self.answers.is_correct_answer("C") == False
        assert self.answers.is_correct_answer("D") == False
