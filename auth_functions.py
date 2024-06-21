import streamlit as st
from firebase_config import auth_pyrebase

def create_account(email, password):
    try:
        user = auth_pyrebase.create_user_with_email_and_password(email, password)
        st.success("Account created successfully")
        return user
    except Exception as e:
        st.error(f"Error creating account: {e}")
        return None

def login(email, password):
    try:
        user = auth_pyrebase.sign_in_with_email_and_password(email, password)
        st.success("Logged in successfully")
        return user
    except Exception as e:
        st.error(f"Error logging in: {e}")
        return None

def send_verification_email(user):
    try:
        auth_pyrebase.send_email_verification(user['idToken'])
        st.success("Verification email sent")
    except Exception as e:
        st.error(f"Error sending verification email: {e}")

def verify_account(id_token):
    try:
        user_info = auth_pyrebase.get_account_info(id_token)
        if user_info['users'][0]['emailVerified']:
            st.success("Email is verified")
            return True
        else:
            st.warning("Email not verified")
            return False
    except Exception as e:
        st.error(f"Error verifying email: {e}")
        return False
