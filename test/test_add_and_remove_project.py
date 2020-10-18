import random
from model.project import Project


def test_add_project_soap(app, json_projects):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    some_project = json_projects
    old_projects = app.soap.get_projects_list(app, username, password)
    app.project.create_project(some_project)
    new_projects = app.soap.get_projects_list(app, username, password)
    assert len(old_projects) + 1 == app.project.count_projects()
    old_projects.append(some_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_remove_project_soap(app, db):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    if len(db.get_tasks_list()) == 0:
        app.project.create_project(Project(name='n_for_del', description='d_for_del'))
    old_projects = app.soap.get_projects_list(app, username, password)
    some_project = random.choice(old_projects)
    app.project.delete_project_by_id(some_project.id)
    new_projects = app.soap.get_projects_list(app, username, password)
    assert len(old_projects) - 1 == app.project.count_projects()
    old_projects.remove(some_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

