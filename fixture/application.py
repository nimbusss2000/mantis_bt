from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == 'chrome':
            self.wd = webdriver.Chrome(executable_path=r'C:\gecko\chromedriver1.exe')
        elif browser == 'firefox':
            self.wd = webdriver.Firefox()
        else:
            raise ValueError('unrecognized browser')
        self.base_url = base_url
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
