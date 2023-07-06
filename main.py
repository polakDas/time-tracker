# Doc: https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/PySimpleGUI.py

import PySimpleGUI as sg

from database.models import create_tables

from ui.menu import create_menu
from ui.shortcuts import create_shortcut
from ui.footer import create_footer

from component import projects_tasks
from component import project
from component import task

def create_todo_gui():
    """
    This function is creating the GUI for this application.
    """
    sg.theme("DarkAmber")
    menu = create_menu()
    shortcut = create_shortcut()
    footer = create_footer()

    projects_tasks_section = projects_tasks.create_projects_tasks_section()

    layout = [
        [menu],
        [shortcut],
        [projects_tasks_section],
        [footer],
    ]

    right_click_menu = ["unused", ["Open", "Quit"]]

    window = sg.Window("Time Tracker Application",
                        layout=layout,
                        right_click_menu=right_click_menu,
                        resizable=True,
                        icon=r"./assets/icon.png",
                        size=(600, 400))  # Adjust the size as per your needs

    tree = window['-PROJECT-TASK-TREE-']
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WINDOW_CLOSED or event == "Quit":
            break
        elif event == "Open":
            pass
            # filename = sg.popup_get_file("File to open", no_window=False)
            # print(filename)
        elif event == "About":
            window.disappear()
            sg.popup('Time Tracker', 'Version 1.0', 'Simple time tracker application', 'Track your time by task')
            window.reappear()
        elif event == "New Project":
            project.project_form(tree)
        elif event == "New Task":
            task.task_form(tree)
        elif event == "-PROJECT-TASK-TREE-":
            if values["-PROJECT-TASK-TREE-"][0].startswith('task-'):  # Check if any item is selected in the tree
                window['-START-TASK-'].update(disabled=False)
                window['-PAUSE-TASK-'].update(disabled=False)
                window['-END-TASK-'].update(disabled=False)
            else:
                window['-START-TASK-'].update(disabled=True)
                window['-PAUSE-TASK-'].update(disabled=True)
                window['-END-TASK-'].update(disabled=True)
        elif event.endswith('-TASK-') and values["-PROJECT-TASK-TREE-"][0].startswith('task-'):
            task.update_task(event=event, value=values["-PROJECT-TASK-TREE-"][0])
            # print(event, values["-PROJECT-TASK-TREE-"])

    window.close()

if __name__ == "__main__":
    create_tables()
    create_todo_gui()
