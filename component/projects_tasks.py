import PySimpleGUI as sg
from database.models import Project, Task

DATA = sg.TreeData()

def load_data():
    # Load projects
    projects = Project.select()
    for project in projects:
        # Insert(Parent, Key, Name, [Values, [*values]])    *if any
        DATA.Insert("", f'project-{project.id}', project.name, [f"{format_duration(project.total_duration)}"])

    # Load tasks
    tasks = Task.select()
    for task in tasks:
        if task.project:
            # Insert(Parent, Key, Name, [Values, [*values]])    *if any
            DATA.Insert(f'project-{task.project.id}', f'task-{task.id}', task.name, [f"{format_duration(task.total_duration)}"])
        else:
            DATA.Insert("Unknown (Default)", f'task-{task.id}', task.name, [f"{format_duration(task.total_duration)}"])

def create_projects_tasks_section():
    load_data()

    project_tree = sg.Tree(data=DATA,
                            headings=["Total time"],
                            col0_heading="Name",
                            justification="right",
                            border_width=2,
                            header_font=("Arial", 12),
                            auto_size_columns=False,
                            key="-PROJECT-TASK-TREE-",
                            select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                            hide_vertical_scroll=True,
                            expand_x=True,
                            expand_y=True,
                            font=("Arial", 11),
                            enable_events=True,
                        )

    layout = [
        [sg.Frame(
            "Projects and Tasks",
            [[project_tree]],
            relief=sg.RELIEF_SUNKEN,
            key="-WHOLE-TREE-",
            expand_x=True,
            expand_y=True,
            pad=(0, 5),
            font=("Arial", 13),
        )]
    ]

    return layout

def update_project_tree(tree, project):
    DATA.Insert("", project.name, project.name, [f"{format_duration(project.total_duration)}"])
    tree.update(DATA)

def update_task_tree(tree, task):
    if task.project:
        DATA.Insert(task.project.name, task.name, task.name, [f"{format_duration(task.total_duration)}"])
    else:
        DATA.Insert("Unknown (Default)", task.name, task.name, [f"{format_duration(task.total_duration)}"])
    tree.update(DATA)


def format_duration(minutes):
    years = minutes // (60 * 24 * 365)
    months = (minutes % (60 * 24 * 365)) // (60 * 24 * 30)
    weeks = (minutes % (60 * 24 * 30)) // (60 * 24 * 7)
    days = (minutes % (60 * 24 * 7)) // (60 * 24)
    hours = (minutes % (60 * 24)) // 60
    minutes = minutes % 60

    duration_parts = []
    if years > 0:
        duration_parts.append(f"{years} yr{'s' if years > 1 else ''}")
    if months > 0:
        duration_parts.append(f"{months} mo{'s' if months > 1 else ''}")
    if weeks > 0:
        duration_parts.append(f"{weeks} wk{'s' if weeks > 1 else ''}")
    if days > 0:
        duration_parts.append(f"{days} d{'s' if days > 1 else ''}")
    if hours > 0:
        duration_parts.append(f"{hours} hr{'s' if hours > 1 else ''}")
    if minutes > 0:
        duration_parts.append(f"{minutes} min{'s' if minutes > 1 else ''}")

    return " ".join(duration_parts)

