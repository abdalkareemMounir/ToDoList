import PySimpleGUI as sg
import functions

label = sg.Text("type in a to do")
input_box = sg.InputText(tooltip="Enter to do",key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),key="todos",
                      enable_events=True,size=[45,10])
window=sg.Window('My To-Do app',layout=[[label],[input_box,add_button]],
                 font=('Helvetica',20))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.set_todos(todos)
        case sg.WIN_CLOSED:
            break

window.read()
window.close()