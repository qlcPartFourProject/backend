import os
from flask_restful import Resource
from flask import make_response, send_file
from firebase_admin import storage, firestore

class ProgramController(Resource):
    def get(self, id: str):
        db = firestore.client()
        program_doc_ref= db.collection('study_programs').document(id)
        program = program_doc_ref.get().to_dict()

        # temporarily store file
        temp_file_path = os.path.join(os.getcwd(), 'temp', program.get('filename'))
        bucket = storage.bucket()
        blob = bucket.blob(program.get('storageKey'))
        blob.download_to_filename(temp_file_path)
        
        # create response
        response = make_response(send_file(temp_file_path, as_attachment=True, download_name=program.get('filename')))
        response.headers['X-Id'] = program_doc_ref.id
        response.headers['X-Author-Id'] = program.get('author').id
        response.headers['Access-Control-Expose-Headers'] = 'X-Id, X-Author-Id, Content-Disposition'

        return response