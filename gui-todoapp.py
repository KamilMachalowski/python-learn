import todoApps_modules as tdm
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=tdm.get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

layout = [
    [label],
    [input_box, add_button],
    [list_box, edit_button]
]

window = sg.Window("My TODO APP",
                   layout=layout,
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = tdm.get_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            tdm.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = tdm.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            tdm.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()