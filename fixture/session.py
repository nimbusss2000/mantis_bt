
class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.open_homepage()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_css_selector('input[type="submit"]').click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def open_homepage(self):
        wd = self.app.wd
        wd.get(self.app.base_url)

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_link_text('administrator').text

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('span[class="user-info"]').click()
        wd.find_element_by_xpath("//a[contains(text(),'Выход')]").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector('span[class="user-info"]')) > 0

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()


