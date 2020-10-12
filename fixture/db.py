
import pymysql.cursors
from model.project import Project


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_project_list(self):
        proj_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('SELECT bug_text_id, summary FROM `mantis_bug_table')
            for row in cursor:
                (id, topic) = row
                proj_list.append(Project(id=str(id), topic=topic))
        finally:
            cursor.close()
        return proj_list

    def destroy(self):
        self.connection.close()