# BACKEND


### In bash
# If you don't have virtualenv installed (optional)
pip install virtualenv 

# From the repo's root dir, go into the backend folder:
cd backend

# Create the virtual environment (only do in first install)
py -m venv .venv

# Activate the virtual environment
source .venv\scripts\activate
.venv\scripts\activate

### In venv
# Install dependencies (only do in first install)
pip install -r requirements.txt 

# Run the application
flask run

### Firebase Setup:
In the Firebase console, open Settings > Service Accounts.
Click Generate New Private Key, then confirm by clicking Generate Key.
Add the following line to the .env file in the backend folder:
```FIREBASE_PRIVATE_KEY_PATH=path_to_generated_file```
DO NOT store the generated file in this repository or push it to GitHub.