from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS
import firebase_admin
from firebase_admin import firestore, credentials, initialize_app, storage 
import os
# VSC thinks dotenv doesn't exist for some reason. 
# This seems to be a bug with VSC. It works when you run it.
from dotenv import load_dotenv

from src.controllers.program.program_controller import ProgramController
from src.controllers.user.user_controller import UserController
from src.controllers.quiz.quiz_list_controller import QuizListController
from src.controllers.quiz.quiz_controller import QuizController
from src.controllers.survey.survey_controller import SurveyController
from src.controllers.test.test_controller import TestController
from src.controllers.feedback.feedback_controller import FeedbackController

from flask import make_response, request

# init firebase client
load_dotenv()
cred = credentials.Certificate(os.getenv("FIREBASE_PRIVATE_KEY_PATH"))
initialize_app(cred, {'storageBucket': 'qlcs-part-4-project.appspot.com'})
db = firestore.client()

# init flask server
app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment this on deployment
api = Api(app)

@app.route('/', defaults={'u_path': ''}, methods=["GET", "OPTIONS"])
@app.route('/<path:u_path>', methods=["GET", "OPTIONS"])
def options(u_path):
    print(u_path, request.method)
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "GET": # The actual request following the preflight
        return _corsify_actual_response(make_response('Hello World!'))
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))

# method for pre-flight request
def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

# add cors to response
def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

api.add_resource(ProgramController, '/api/program/<id>')
api.add_resource(UserController, '/api/user/<id>')
api.add_resource(QuizListController, '/api/quiz')
api.add_resource(QuizController, '/api/quiz/<id>')
api.add_resource(SurveyController, '/api/survey/<id>')
api.add_resource(FeedbackController, '/api/feedback/<id>')
api.add_resource(TestController, '/api/test')