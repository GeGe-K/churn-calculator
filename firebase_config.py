import firebase_admin
from firebase_admin import credentials, auth
import pyrebase

# Your Firebase configuration object
firebaseConfig = {
    'apiKey': "AIzaSyAOaLQ5Ado8xNy1sZ9VTMA8iV6dpeprtfE",
    'authDomain': "churn-predictor-app.firebaseapp.com",
    'projectId': "churn-predictor-app",
    'storageBucket': "churn-predictor-app.appspot.com",
    'messagingSenderId': "176298143632",
    'appId': "1:176298143632:web:970936f54a1a570b7f4d15",
    'measurementId': "G-522RVB3RSM",
    'databaseURL': "https://churn-predictor-app-default-rtdb.firebaseio.com/"
}

# Initialize Firebase Admin SDK
cred = credentials.Certificate("/Firebase/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Initialize Pyrebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth_pyrebase = firebase.auth()
