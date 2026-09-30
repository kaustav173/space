import streamlit as st

st.set_page_config(page_title="My Hugging Face App")

st.title("🚀 My Hugging Face Space")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Hello {name}!")

st.write("This application is deployed using GitHub Actions.")