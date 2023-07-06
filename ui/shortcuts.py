import PySimpleGUI as sg

def create_shortcut():
    # Set the background color of the buttons to match the window's background color
    button_color = ('white', sg.theme_background_color())

    # Create the layout with evenly spaced buttons
    shortcut_def = [
        sg.Button('Start', button_color=button_color, expand_x=True, disabled=True, key='-START-TASK-', font=("Arial", 11)),
        sg.VerticalSeparator(),
        sg.Button('Pause', button_color=button_color, expand_x=True, disabled=True,key='-PAUSE-TASK-', font=("Arial", 11)),
        sg.VerticalSeparator(),
        sg.Button('Stop & Save', button_color=button_color, expand_x=True, disabled=True,key='-END-TASK-', font=("Arial", 11)),
    ]

    shortcut_row = [shortcut_def]  # Place the buttons in a list

    return shortcut_row
