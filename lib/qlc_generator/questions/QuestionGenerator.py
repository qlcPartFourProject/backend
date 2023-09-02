from lib.qlc_generator.questions.Question import Question

class QuestionGenerator():
    def __init__(self, astUtil):
        self.astUtil = astUtil

    def generate_question(self, question_type: Question):
        question: Question =  question_type(self.astUtil)

        # AST node to quiz on
        question.select_node()

        # add correct answer
        question.generate_correct_answer()

        # add distractors
        question.generate_distractors()

        question.create_question_text()
        question.create_answer_options()

        return question
