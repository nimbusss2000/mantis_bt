import random

from model.project import Project


def test_add_project_json(app, db, json_projects):
    some_project = json_projects
    old_projects = db.get_project_list()
    app.project.create(some_project)
    new_projects = db.get_project_list()
    assert len(old_projects) + 1 == app.project.count()
    old_projects.append(some_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_add_project_model(app, db, data_projects):
    some_project = data_projects
    old_projects = db.get_project_list()
    app.project.create(some_project)
    new_projects = db.get_project_list()
    assert len(old_projects) + 1 == app.project.count()
    old_projects.append(some_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_remove_project(app, db):
    if len(db.get_project_list()) == 0:
        app.group.create(Project(topic='t_for_del', description='d_for_del'))
    old_projects = db.get_project_list()
    some_project = random.choice(old_projects)
    app.project.delete_project_by_id(some_project.id)
    new_projects = db.get_project_list()
    assert len(old_projects) - 1 == app.project.count()
    old_projects.remove(some_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

