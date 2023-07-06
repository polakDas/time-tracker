import PySimpleGUI as sg

def create_menu():
    menu_def = [
        [
            "&Files",
            ["&Open", "&Save", "&Export", "&Quit"],
            {'font': ('Arial', 18)}
        ],
        [
            "&Project",
            ["New P&roject",
            "Edit Pro&ject",
            "New T&ask",
            "Edit Tas&k",
            "New S&ub-Task",
            "Edit Su&b-Task"],
            {'font': ('Arial', 12)}
        ],
        [
            "&About",
            ["About"],
            {'font': ('Arial', 12)}
        ]
    ]

    menu = sg.Menu(menu_def, pad=(2,2), key="-CUSTOM_MENUBAR-", font=("Arial", 11))

    return menu