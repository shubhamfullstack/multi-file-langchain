import streamlit as st
import os
from upload import page_upload
from chat import page_chat
from files import show_files
from apikey import apikey

import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth

os.environ["OPENAI_API_KEY"] = apikey

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.title("📁 Fusion AI")
    st.subheader("Explore the power of Generative AI with your own pdfs")
    upload, chat,files, prompts, settings = st.tabs(["Upload", "Chat","Files", "Prompt Templates","Settings"])

    with upload:
        page_upload()

    with chat:
        page_chat()

    with files:
        show_files()
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')