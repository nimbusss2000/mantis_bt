import random

from model.task import Task


def test_add_task_json(app, db, json_tasks):
    some_task = json_tasks
    old_tasks = db.get_tasks_list()
    app.project.create_task(some_task)
    new_tasks = db.get_tasks_list()
    assert len(old_tasks) + 1 == app.project.count_tasks()
    old_tasks.append(some_task)
    assert sorted(old_tasks, key=Task.id_or_max) == sorted(new_tasks, key=Task.id_or_max)


def test_add_task_model(app, db, data_tasks):
    some_task = data_tasks
    old_projects = db.get_tasks_list()
    app.project.create_task(some_task)
    new_tasks = db.get_tasks_list()
    assert len(old_projects) + 1 == app.project.count_tasks()
    old_projects.append(some_task)
    assert sorted(old_projects, key=Task.id_or_max) == sorted(new_tasks, key=Task.id_or_max)


def test_remove_task(app, db):
    if len(db.get_tasks_list()) == 0:
        app.group.create_task(Task(topic='t_for_del', description='d_for_del'))
    old_tasks = db.get_tasks_list()
    some_task = random.choice(old_tasks)
    app.project.delete_task_by_id(some_task.id)
    new_projects = db.get_tasks_list()
    assert len(old_tasks) - 1 == app.project.count_tasks()
    old_tasks.remove(some_task)
    assert sorted(old_tasks, key=Task.id_or_max) == sorted(new_projects, key=Task.id_or_max)

