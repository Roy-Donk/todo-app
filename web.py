import streamlit as st

import functions

file_name = "files/todo.txt"
file_directory = "../files/"

todos = functions.loadList(file_name)


# if 'new_todo' not in st.session_state:
#     st.session_state['new_todo'] = ''

def add_todo():
    todo_local = st.session_state["new_todo"]
    todos.append(todo_local)
    st.session_state["new_todo"] = ""
    functions.updateFileList(file_name, todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

#
for index, todo in enumerate(todos):
    checkbox_key = f"{index}-{todo}"
    checkbox = st.checkbox(todo, key=checkbox_key)
    if checkbox:
        todos.pop(index)
        functions.updateFileList(file_name, todos)
        del st.session_state[checkbox_key]
        st.experimental_rerun()

st.text_input(label="Add a new todo", key='new_todo', on_change=add_todo)

st.write(st.session_state)
