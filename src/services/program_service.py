import os
import uuid
from firebase_admin import  storage, firestore

filename_delimiter = '_-_'

def get_file(url):
    bucket = storage.bucket()
    blob = bucket.blob(url)
    with blob.open("r") as f:
        return f.read()
    
def get_file_v2():
    pass

def create_program(filename, temp_file_path):
    # save file to bucket
    bucket = storage.bucket()
    storageKey = os.path.splitext(filename)[0] + filename_delimiter + str(uuid.uuid4()) + '.py'
    new_blob_ref = bucket.blob(storageKey) # get new blob ref from storage
    new_blob_ref.upload_from_filename(temp_file_path) # set temp file as content for blob

    db = firestore.client()
    author_doc_ref = db.collection('Users').document('QTo77wjVwQTAKIuzw5nX8VKKyTG3')
    new_program_doc_ref= db.collection('programs').document()
    new_program_doc_ref.set({
        'author': author_doc_ref,
        'filename': filename,
        'storageKey': storageKey
    })

    # new_program = new_program_doc.to_dict()

    return {
        '_id': new_program_doc_ref.id,
        'authorId': author_doc_ref.id
    }

def get_program_by_id(id: str):
    pass