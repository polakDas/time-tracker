

import PySimpleGUI as sg

def create_footer():
    footer_def = [
        # Horizontal separator
        [sg.HorizontalSeparator()],
        # Footer section
        [sg.Text("You've spent total of 2 hours today.")]
    ]

    footer = [footer_def]

    return footer