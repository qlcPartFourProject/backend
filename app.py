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

# init firebase client
load_dotenv()
cred = credentials.Certificate(os.getenv("FIREBASE_PRIVATE_KEY_PATH"))
initialize_app(cred, {'storageBucket': 'qlcs-part-4-project.appspot.com'})
db = firestore.client()

# init flask server
app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(ProgramController, '/api/program/<id>')
api.add_resource(UserController, '/api/user/<id>')
api.add_resource(QuizListController, '/api/quiz')
api.add_resource(QuizController, '/api/quiz/<id>')
api.add_resource(SurveyController, '/api/survey/<id>')
api.add_resource(TestController, '/api/test')