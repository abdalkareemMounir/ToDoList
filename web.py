import streamlit as st
import functions

todos = functions.get_todos()
st.title("My to-do App")
st.subheader("this is my todo app")

st.write("this app increase your productivety")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo...")