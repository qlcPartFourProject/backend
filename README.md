# Backend Setup (local environment):

1) In a terminal, navigate to the root of the backend folder: `cd /PATH_TO_ROOT`
2) If you don't have virtualenv installed (optional): `pip install virtualenv`
3) Create the virtual environment (only do in first install): `py -m venv .venv`
4) Activate the virtual environment: `.venv\scripts\activate`
5) Install dependencies (only do in first install): `pip install -r requirements.txt`
6) Run the application: `flask run`

# Firebase Setup (local environment):
1) In the Firebase console, open Settings > Service Accounts.
2) Click Generate New Private Key, then confirm by clicking Generate Key.
3) Add the following line to the .env file in the backend folder: ```FIREBASE_PRIVATE_KEY_PATH=path_to_generated_file```
Note: DO NOT store the generated file in this repository or push it to GitHub.
