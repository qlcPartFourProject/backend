from src.dtos.quiz.create_submission import CreateSubmission
from firebase_admin import firestore
from firebase_admin.firestore import SERVER_TIMESTAMP

def add_survey_results(create_submission: CreateSubmission):
    db = firestore.client()
    new_submission_ref = db.collection('exhibition_day_quizzes', create_submission.quiz_id, 'survey' ).document()

    submission_data = {
        'created': SERVER_TIMESTAMP,
        'quizId': create_submission.quiz_id,
        'answers': create_submission.answers
    }
    
    new_submission_ref.set(submission_data)

    return new_submission_ref.id