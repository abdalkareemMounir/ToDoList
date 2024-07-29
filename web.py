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

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.set_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todo,key="new_todo")

st.session_state