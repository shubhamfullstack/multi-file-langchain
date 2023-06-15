import streamlit as st
import os

def show_files():
    files = os.listdir("data")
    st.write("Uploaded Files:")
    for file in files:
        st.write("- " + file)