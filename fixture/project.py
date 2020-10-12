

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get('http://localhost/mantisbt-2.24.2/view_all_bug_page.php')

    def create(self, project):
        wd = self.app.wd
        self.open_home_page()
        self.fill_project_form(project)
        wd.find_element_by_css_selector(".btn-white").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.choose_project()
        wd.find_element_by_id("handler_id").click()
        dropdown = wd.find_element_by_id("handler_id")
        dropdown.find_element_by_xpath(f"//option[. = 'administrator']").click()
        wd.find_element_by_id("handler_id").click()
        wd.find_element_by_id("summary").click()
        wd.find_element_by_id("summary").send_keys(project.topic)
        wd.find_element_by_id("description").click()
        wd.find_element_by_id("description").send_keys(project.description)

    def choose_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='sidebar']/ul/li[3]/a/i").click()
        if len(wd.find_elements_by_xpath("//form[@id='select-project-form']/div/div[2]/div[2]/input")) > 0:
            wd.find_element_by_xpath("//form[@id='select-project-form']/div/div[2]/div[2]/input").click()
        else:
            return

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        trs = wd.find_elements_by_css_selector('tbody')[1]
        return len(trs.find_elements_by_css_selector('tr'))

    group_cache = None

    def select_project_by_id(self, project_id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f'a[href="/mantisbt-2.24.2/view.php?id={project_id}"]').click()

    def delete_project_by_id(self, project_id):
        wd = self.app.wd
        self.open_home_page()
        self.select_project_by_id(project_id)
        wd.find_element_by_css_selector(".pull-left:nth-child(9) .btn").click()
        wd.find_element_by_css_selector(".btn-white").click()
        self.group_cache = None

    # def get_project_list(self):
    #     if self.group_cache is None:
    #         wd = self.app.wd
    #         self.open_home_page()
    #         self.group_cache = []
    #         for td in wd.find_elements_by_css_selector('tr'):
    #             id = td.find_element_by_css_selector('td.column-id').text
    #             # tr = td.find_element_by_css_selector('td[class="column-selection"]')
    #             # trr = tr.find_element_by_css_selector('div[class="checkbox no-padding no-margin"]')
    #             # id = trr.find_element_by_css_selector('label.input[type="checkbox"]').get_attribute('value')
    #
    #             text = td.find_element_by_css_selector('td[class="column-summary"]').text
    #             self.group_cache.append(Project(name=text, id=id))
    #     return list(self.group_cache)