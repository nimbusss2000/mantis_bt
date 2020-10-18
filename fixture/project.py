

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get('http://localhost/mantisbt-2.24.2/view_all_bug_page.php')

    def create_task(self, task):
        wd = self.app.wd
        self.open_home_page()
        self.fill_task_form(task)
        wd.find_element_by_css_selector(".btn-white").click()

    def fill_task_form(self, task):
        wd = self.app.wd
        self.choose_task()
        wd.find_element_by_id("handler_id").click()
        dropdown = wd.find_element_by_id("handler_id")
        dropdown.find_element_by_xpath(f"//option[. = 'administrator']").click()
        wd.find_element_by_id("handler_id").click()
        wd.find_element_by_id("summary").click()
        wd.find_element_by_id("summary").send_keys(task.topic)
        wd.find_element_by_id("description").click()
        wd.find_element_by_id("description").send_keys(task.description)

    def choose_task(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='sidebar']/ul/li[3]/a/i").click()
        if len(wd.find_elements_by_xpath("//form[@id='select-project-form']/div/div[2]/div[2]/input")) > 0:
            wd.find_element_by_xpath("//form[@id='select-project-form']/div/div[2]/div[2]/input").click()
        else:
            return

    def count_tasks(self):
        wd = self.app.wd
        self.open_home_page()
        trs = wd.find_elements_by_css_selector('tbody')[1]
        return len(trs.find_elements_by_css_selector('tr'))

    group_cache = None

    def select_task_by_id(self, project_id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f'a[href="/mantisbt-2.24.2/view.php?id={project_id}"]').click()

    def delete_task_by_id(self, project_id):
        wd = self.app.wd
        self.open_home_page()
        self.select_task_by_id(project_id)
        wd.find_element_by_css_selector(".pull-left:nth-child(9) .btn").click()
        wd.find_element_by_css_selector(".btn-white").click()
        self.group_cache = None


    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('a[href="/mantisbt-2.24.2/manage_overview_page.php"]').click()
        wd.find_element_by_css_selector('a[href="/mantisbt-2.24.2/manage_proj_page.php"]').click()

    def create_project(self, project):
        wd = self.app.wd
        # self.open_home_page()
        self.open_projects_page()
        wd.find_element_by_css_selector('button[type="submit"]').click()
        self.fill_project_form(project)
        wd.find_element_by_link_text("Продолжить").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").send_keys(project.name)
        wd.find_element_by_id("project-description").click()
        wd.find_element_by_id("project-description").send_keys(project.description)
        wd.find_element_by_css_selector(".btn-white").click()

    def count_projects(self):
        wd = self.app.wd
        # self.open_home_page()
        self.open_projects_page()
        trs = wd.find_elements_by_css_selector('tbody')[0]
        count = trs.find_elements_by_css_selector('tr')
        return len(count)

    def delete_project_by_id(self, project_id):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector(f'a[href="manage_proj_edit_page.php?project_id={project_id}"]').click()
        wd.find_element_by_css_selector(".btn:nth-child(3)").click()
        wd.find_element_by_css_selector(".btn-white").click()

