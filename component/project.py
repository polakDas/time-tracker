import PySimpleGUI as sg
from database.models import Project

from component import projects_tasks

def project_form(tree):
    # Define the layout of the form
    layout = [
        [sg.Column([[sg.Text("WTF! You got a new Project? Let's register", font=("Roboto", 18))]], justification="center")],
        [sg.HorizontalSeparator(pad=(80, 10), color="gray")],

        [sg.Text("Project Name:", size=(18, 1)), sg.Input(key="-NAME-", size=(50, 1))],
        [sg.Text("Description:", size=(18, 1)), sg.Multiline(key="-DESCRIPTION-", no_scrollbar=True, size=(50, 10))],
        [sg.Text("Select start date:", size=(18, 1)), sg.Input(key="-START-DATE-", enable_events=True, size=(30, 1)),
            sg.CalendarButton("Choose Date", target="-START-DATE-", format="%d-%m-%Y", button_color=("white", "gray"), size=(15, 1))],
        [sg.Text("Select end date:", size=(18, 1)), sg.Input(key="-END-DATE-", enable_events=True, size=(30, 1)),
            sg.CalendarButton("Choose Date", target="-END-DATE-", format="%d-%m-%Y", button_color=("white", "gray"), size=(15, 1))],
        [sg.Text("Time Worked:", size=(18, 1)), sg.Input(key="-DURATION-", size=(50, 1))],
        
        [sg.Button("Create"), sg.Button("Cancel")]
    ]

    # Create the form window
    form_window = sg.Window("New Project", layout)

    while True:
        form_event, form_values = form_window.read()

        if form_event == "Cancel" or form_event == sg.WINDOW_CLOSED:
            # Close the form if the user cancels or closes the window
            break

        elif form_event == "Create":
            # Retrieve the entered values from the form
            project_name = form_values["-NAME-"]
            project_description = form_values["-DESCRIPTION-"]
            project_start_date = form_values["-START-DATE-"]
            project_end_date = form_values["-END-DATE-"]
            project_duration = form_values["-DURATION-"]

            # Perform any validation or data processing here

            # Create the project using the retrieved values
            create_project(
                tree=tree,
                name=project_name,
                description=project_description,
                start_date=project_start_date,
                expected_end_date=project_end_date,
                total_duration=project_duration,
            )

            # Close the form
            break

    # Close the form window
    form_window.close()

def create_project(tree,
                name,
                description=None,
                start_date=None,
                expected_end_date=None,
                end_date=None,
                total_duration=None):
    if name is None or name == "":
        # sg.popup_button_error("Error")
        sg.popup_error(
            "Name must be provided",
            "WTF BRO!! How can you create a project without project name??",
            "Please enter a meaningful project name.",
            "Thanks",
            text_color='#e33030',
            no_titlebar=True,
        )
        return project_form()
    project_data = {
        'name': name,
    }

    if description is not None:
        project_data['description'] = description
    if start_date is not None and start_date != "":
        project_data['start_date'] = start_date
    if expected_end_date is not None and expected_end_date != "":
        project_data['expected_end_date'] = expected_end_date
    if end_date is not None and end_date != "":
        project_data['end_date'] = end_date
    if total_duration is not None and total_duration != "":
        project_data['total_duration'] = total_duration

    new_project = Project.create(**project_data)
    print(f"{new_project.name} has been created")
    projects_tasks.update_project_tree(tree=tree, project=new_project)

# class Project:
#     def __init__(self, name):
#         self.name = name
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def remove_task(self, task):
#         self.tasks.remove(task)


# class ProjectManager:
#     def __init__(self):
#         self.projects = []

#     def add_project(self, project):
#         self.projects.append(project)

#     def remove_project(self, project):
#         self.projects.remove(project)

#     def get_project_names(self):
#         return [project.name for project in self.projects]
