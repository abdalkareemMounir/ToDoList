import streamlit as st
import functions

todos = functions.get_todos()
print(todos)
print("hello")
def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.set_todos(todos)
    
st.title("My to-do App")
st.subheader("this is my todo app")

st.write("this app increase your productivety")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todo,key="new_todo")