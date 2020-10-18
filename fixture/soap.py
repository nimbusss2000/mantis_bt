
from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, app, username, password):
        client = Client(app.config['soap']['wsdl'])
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, app, username, password):
        proj_list = []
        client = Client(app.config['soap']['wsdl'])
        try:
            c = client.service.mc_projects_get_user_accessible(username, password)
            for row in c:
                id = row[0]
                name = row[1]
                proj_list.append(Project(id=str(id), name=name))
            return proj_list
        except WebFault:
            return False