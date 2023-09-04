from src.dtos.feedback.feedback_submission import FeedbackSubmission
from firebase_admin import firestore
from firebase_admin.firestore import SERVER_TIMESTAMP

def add_feedback_results(feedback_submission: FeedbackSubmission):
    db = firestore.client()
    new_submission_ref = db.collection('quizzes', feedback_submission.quiz_id, 'feedback' ).document()

    submission_data = {
        'created': SERVER_TIMESTAMP,
        'quizId': feedback_submission.quiz_id,
        'text': feedback_submission.text
    }

    new_submission_ref.set(submission_data)

    return new_submission_ref.id