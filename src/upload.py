import streamlit as st
from utils.injest import injest
import os


def save_uploaded_file(uploaded_file):
    st.spinner(text="In progress...")
    with open(os.path.join("data", uploaded_file.name), "wb") as file:
        file.write(uploaded_file.getbuffer())
    st.success("Files uploaded successfully!")


def create_vector_store(uploaded_file):
    st.spinner(text="In progress...")
    print("data/" + uploaded_file.name)
    file_extension = uploaded_file.name.split(".")[-1]
    injest("data/" + uploaded_file.name, "."+file_extension)
    st.success("Vector Store is Created Successfully!")


def page_upload(sidebar):
    st.subheader("Upload Multiple PDFs")
    uploaded_file = st.file_uploader(
        "Choose .txt,.pdf,.csv,.doc file",
        type=["pdf", "csv", "txt", "doc", "docx"],
        help="You can upload multiple files.",
        accept_multiple_files=False,
    )
    if uploaded_file:
        save_uploaded_file(uploaded_file)
        create_vector_store(uploaded_file)
        sidebar.write("- " + uploaded_file.name)
