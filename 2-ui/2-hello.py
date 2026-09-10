import streamlit as st

st.title("Saying Hello.")
name = st.text_input("And you are?")
age = st.slider("How old are you?", min_value=18, max_value=100)

mybutton = st.button("GO FOR IT", type="primary")

if name:
    st.write(f"Hello, {name}!")