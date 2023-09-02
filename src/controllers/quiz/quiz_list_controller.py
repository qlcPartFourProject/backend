import os
from flask_restful import Resource
from flask import make_response, request
from src.services.quiz_service import get_all_quizzes, create_quiz
from src.services.program_service import create_program

class QuizListController(Resource):
    def get(self):
        data = { 'results': get_all_quizzes()}

        return make_response(data, 200)
    
    def post(self):
        file = request.files.get("file") # note that a file can only be read ONCE
        print('file', file.filename)
        # save file temporarily
        temp_file_path = os.path.join(os.getcwd(), 'temp', file.filename)
        file.save(temp_file_path) # saving performs a READ on the file

        # save file to bucket
        new_program = create_program(file.filename, temp_file_path)

        # read content of temp file to create the quiz
        with open(temp_file_path, "r") as temp_file:
            temp_content = temp_file.read() # string value

        # delete temp file once complete
        os.remove(temp_file_path) 

        data = create_quiz(new_program.get('_id'), temp_content)

        return make_response(data, 201)