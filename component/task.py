import PySimpleGUI as sg
from database.models import Task, Project

from component import projects_tasks
from component import tracker

def task_form(tree):

    project_names = [(project.id, project.name) for project in Project.select()]
    
    # Define the layout of the form
    layout = [
        [sg.Column([[sg.Text("Found a new task? Let's register", font=("Roboto", 18))]], justification="center")],
        [sg.HorizontalSeparator(pad=(80, 10), color="gray")],

        [sg.Text("Task Name:", size=(18, 1)), sg.Input(key="-NAME-", size=(50, 1))],
        [sg.Text("Description:", size=(18, 1)), sg.Multiline(key="-DESCRIPTION-", no_scrollbar=True, size=(50, 10))],
        [sg.Text("Select a Project:", size=(18, 1)), sg.Combo(values=project_names, key="-PROJECT-", size=(30, 1))],
        [sg.Text("Select start date:", size=(18, 1)), sg.Input(key="-START-DATE-", enable_events=True, size=(30, 1)),
            sg.CalendarButton("Choose Date", target="-START-DATE-", format="%d-%m-%Y", button_color=("white", "gray"), size=(15, 1))],
        [sg.Text("Select end date:", size=(18, 1)), sg.Input(key="-END-DATE-", enable_events=True, size=(30, 1)),
            sg.CalendarButton("Choose Date", target="-END-DATE-", format="%d-%m-%Y", button_color=("white", "gray"), size=(15, 1))],
        [sg.Text("Time Worked:", size=(18, 1)), sg.Input(key="-DURATION-", size=(50, 1))],
        
        [sg.Button("Create"), sg.Button("Cancel")]
    ]

    # Create the form window
    form_window = sg.Window("New Task", layout)

    while True:
        form_event, form_values = form_window.read()

        if form_event == "Cancel" or form_event == sg.WINDOW_CLOSED:
            # Close the form if the user cancels or closes the window
            break

        elif form_event == "Create":
            # Retrieve the entered values from the form
            task_name = form_values["-NAME-"]
            task_description = form_values["-DESCRIPTION-"]
            task_project = form_values["-PROJECT-"]
            task_start_date = form_values["-START-DATE-"]
            task_end_date = form_values["-END-DATE-"]
            task_duration = form_values["-DURATION-"]

            # TODO: Perform any validation or data processing here

            # Select the id if project is given
            task_project_id = task_project[0] if isinstance(task_project, tuple) else None

            # Create the task using the retrieved values
            create_task(
                tree=tree,
                name=task_name,
                description=task_description,
                project_id=task_project_id,
                start_date=task_start_date,
                end_date=task_end_date,
                total_duration=task_duration,
            )

            # Close the form
            break

    # Close the form window
    form_window.close()

def create_task(tree,
                name,
                description=None,
                project_id=None,
                start_date=None,
                end_date=None,
                total_duration=None):
    if name is None or name == "":
        # sg.popup_button_error("Error")
        sg.popup_error("Error", "Name must be provided")
        return task_form
    task_data = {
        'name': name,
    }

    if description is not None:
        task_data['description'] = description
    if project_id is not None and project_id != "":
        task_data['project_id'] = project_id
    if end_date is not None and end_date != "":
        task_data['expected_end_date'] = end_date
    if start_date is not None and start_date != "":
        task_data['start_date'] = start_date
    if total_duration is not None and total_duration != "":
        task_data['total_duration'] = total_duration

    print(task_data)
    # return
    new_task = Task.create(**task_data)
    print(f"{new_task.name} has been created")
    projects_tasks.update_task_tree(tree=tree, task=new_task)


ongoing_tasks = {}  # Dictionary to store ongoing tasks
def update_task(event, value):
    task_id = int(value.split('-')[-1])

    if event == '-START-TASK-':
        if task_id not in ongoing_tasks:
            ongoing_tasks[task_id] = tracker.TimeTracker()  # Create a new TimeTracker instance for the task
            ongoing_tasks[task_id].start_tracker()

    if event == '-PAUSE-TASK-':
        if task_id in ongoing_tasks:
            ongoing_tasks[task_id].pause_tracker()

    if event == '-END-TASK-':
        if task_id in ongoing_tasks:
            ongoing_tasks[task_id].stop_tracker()
            del ongoing_tasks[task_id]  # Remove the task from the ongoing tasks dictionary

# class Task:
#     def __init__(self, name):
#         self.name = name
#         self.subtasks = []

#     def add_subtask(self, subtask):
#         self.subtasks.append(subtask)

#     def remove_subtask(self, subtask):
#         self.subtasks.remove(subtask)


# class TaskManager:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def remove_task(self, task):
#         self.tasks.remove(task)

#     def get_task_names(self):
#         return [task.name for task in self.tasks]
