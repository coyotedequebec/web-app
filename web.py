import streamlit as st
import functions


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    #print(todo)


todos = functions.get_todos()

st.title("My to do app.")
st.subheader("This is my to do app.")
st.write("No need of deployment")

# st.checkbox("Buy Grosseries")
# st.checkbox("New Buy Grosseries")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="box", placeholder="Add a new todo",
              on_change=add_todo, key='new_todo')

print("Hello")
st.session_state
