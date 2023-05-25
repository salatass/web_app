import streamlit as st
import functions as ft

todos = ft.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    ft.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This is to keep track of stuff")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        ft.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", label_visibility="hidden", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

