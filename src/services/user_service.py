from firebase_admin import firestore

def get_all_users():
    db = firestore.client()
    user_docs = db.collection("Users").stream()

    return user_docs

def get_user(id):
    db = firestore.client()
    user_ref = db.collection("Users").document(id)
    user = user_ref.get()
    return user

def create_user(user_args):
    db = firestore.client()
    db.collection("Users").document(user_args.uid).set({'email': user_args.email, 'firstName': user_args.firstName, 'lastName': user_args.lastName})