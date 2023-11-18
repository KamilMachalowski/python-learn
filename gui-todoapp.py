import todoApps_modules
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My TODO APP", layout=[[label], [input_box, add_button]])
window.read()
window.close()