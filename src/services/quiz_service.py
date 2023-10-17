from firebase_admin import firestore
from firebase_admin.firestore import SERVER_TIMESTAMP
import random

# qlc generator
import ast
from lib.qlc_generator.util.Analyzer import Analyzer
from lib.qlc_generator.questions.QuestionGenerator import QuestionGenerator
from lib.qlc_generator.questions.QuestionSeries import QuestionSeries
from lib.qlc_generator.questions.FunctionNameQuestion import FunctionNameQuestion 
from lib.qlc_generator.questions.FunctionParameterListQuestion import FunctionParameterListQuestion
from lib.qlc_generator.questions.LineAtEndOfLoopQuestion import LineAtEndOfLoopQuestion
from lib.qlc_generator.questions.DoesFunctionHaveDependenciesQuestion import DoesFunctionHaveDependenciesQuestion
from lib.qlc_generator.questions.NumberOfFunctionDependenciesQuestion import NumberOfFunctionDependenciesQuestion
from lib.qlc_generator.questions.FunctionDependencyListQuestion import FunctionDependencyListQuestion
from lib.qlc_generator.questions.IsFunctionRecursiveQuestion import IsFunctionRecursiveQuestion
from lib.qlc_generator.questions.NumberOfFunctionParametersQuestion import NumberOfFunctionParametersQuestion
from lib.qlc_generator.questions.FunctionVariableNameListQuestion import FunctionVariableNameListQuestion
from lib.qlc_generator.questions.NumberOfFunctionLoopsQuestion import NumberOfFunctionLoopsQuestion
from lib.qlc_generator.questions.LineInSameLoopQuestion import LineInSameLoopQuestion
from lib.qlc_generator.questions.LineInSameConditionalQuestion import LineInSameConditionalQuestion


from src.models.quiz import Submission
from src.dtos.quiz.create_submission import CreateSubmission


def get_all_quizzes():
    db = firestore.client()

    quizzes_ref= db.collection('exhibition_day_quizzes')
    quizzes = []
    for quiz_doc in quizzes_ref.stream():
         quizzes.append(get_quiz_by_id(quiz_doc.id))
    
    return quizzes


def get_quiz_by_id(id: str):
    db = firestore.client()

    quiz_ref = db.collection('exhibition_day_quizzes').document(id)
    quiz_dict = quiz_ref.get().to_dict()

    questions_ref = db.collection("exhibition_day_quizzes", quiz_ref.id, "questions")
    program_ref = quiz_dict.get('program')
    
    questions = []
    for question_doc in questions_ref.stream():
        question = question_doc.to_dict()
        choices_ref = db.collection("exhibition_day_quizzes", quiz_ref.id, "questions", question_doc.id, "choices")
        
        choices = []
        for choice_doc in choices_ref.stream():
            choice = choice_doc.to_dict()
            choice['_id'] = choice_doc.id
            choices.append(choice)

        question['_id'] = question_doc.id
        question['choices'] = choices
        questions.append(question)

    return {
        '_id': quiz_ref.id,
        'programId': program_ref.id,
        'questions': questions,
    }


def create_quiz(program_id, file_content):
        # read file as ast
        tree = ast.parse(file_content)

        # # analyze AST contents
        analyzer = Analyzer()
        analyzer.visit(tree)

        question_generator = QuestionGenerator(analyzer.astUtil)

        question_types = [
             FunctionNameQuestion,
             FunctionParameterListQuestion,
             LineAtEndOfLoopQuestion,
             DoesFunctionHaveDependenciesQuestion,
             NumberOfFunctionDependenciesQuestion,
             FunctionDependencyListQuestion,
             IsFunctionRecursiveQuestion,
             NumberOfFunctionParametersQuestion,
             FunctionVariableNameListQuestion,
             NumberOfFunctionLoopsQuestion,
             LineInSameLoopQuestion,
             LineInSameConditionalQuestion
        ]

        generated_questions = []
        
        for q_type in question_types:
            try:
                generated_questions.append(
                    question_generator.generate_question(q_type)
                )
            except:
                pass
            
        random.shuffle(generated_questions)
        quiz_questions = generated_questions[:5]
        
        # create quiz data
        db = firestore.client()

        program_doc_ref = db.collection('exhibition_day_programs').document(program_id)
        new_quiz_data = { 'program' : program_doc_ref }
        new_quiz_doc_ref= db.collection('exhibition_day_quizzes').document()
        new_quiz_doc_ref.set(new_quiz_data)

        for i, question in enumerate(quiz_questions):
            question_json = question.json()
            new_question_data = { 
                'text': question_json.get('text'),
                'type': question_json.get('type')
            }
            new_question_doc_ref = db.collection('exhibition_day_quizzes', new_quiz_doc_ref.id, 'questions').document(str(i))
            new_question_doc_ref.set(new_question_data)
            
            for j, choice_json in enumerate(question_json.get('choices')) :
                new_choice_doc_ref = db.collection('exhibition_day_quizzes', new_quiz_doc_ref.id, 'questions', new_question_doc_ref.id, 'choices' ).document(str(j))
                new_choice_doc_ref.set(choice_json)

        return {
            'quizId': new_quiz_doc_ref.id
        }

def create_quiz_submission(create_submission: CreateSubmission):
    # create quiz data
    db = firestore.client()
    new_submission_ref = db.collection('exhibition_day_quizzes', create_submission.quiz_id, 'submissions' ).document()
    submission_data = {
        'created': SERVER_TIMESTAMP,
        'quizId': create_submission.quiz_id,
        'answers': create_submission.answers
    }
    
    new_submission_ref.set(submission_data)

    return new_submission_ref.id