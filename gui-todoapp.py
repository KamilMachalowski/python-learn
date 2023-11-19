import todoApps_modules as tdm
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My TODO APP",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = tdm.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            tdm.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()