import peewee
from datetime import datetime

from database.connection import BaseModel, db

class Project(BaseModel):
    name = peewee.CharField(max_length=100, unique=True, help_text="Project name")
    description = peewee.TextField(null=True, help_text="Project description")
    start_date = peewee.DateTimeField(default=datetime.now, help_text="Project start date")
    expected_end_date = peewee.DateTimeField(null=True, help_text="Expected end date")
    end_date = peewee.DateTimeField(null=True, help_text="Project end date")
    total_duration = peewee.IntegerField(default=0, help_text="Total duration for the project")

    def calculate_total_duration(self):
        total_duration = Task.select(fn.Sum(Task.total_duration)).where(Task.project == self).scalar()
        self.total_duration = total_duration or 0
        self.save()

class Task(BaseModel):
    name = peewee.CharField(max_length=100, help_text="Task name")
    description = peewee.TextField(null=True, help_text="Task description")
    project = peewee.ForeignKeyField(Project, backref="tasks", on_delete="SET NULL", null=True)
    task = peewee.ForeignKeyField('self', backref='subtasks', on_delete='SET NULL', null=True)
    start_date = peewee.DateTimeField(default=datetime.now, help_text="Task start date")
    expected_end_date = peewee.DateTimeField(null=True, help_text="Expected end date")
    end_date = peewee.DateTimeField(null=True, help_text="Task end date")
    total_duration = peewee.IntegerField(default=0, help_text="Total time spent for this task")

def create_tables():
    with db:
        db.create_tables([Project, Task])
        try:
            Project.create(name="Unknown (Default)", description="This is a default project. Don't delete this. All the tasks with no project will stay there.")
        except:
            pass

create_tables()  # Call the function to create tables
