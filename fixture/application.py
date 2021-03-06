from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SigupHelper
from fixture.soap import SoapHelper
from fixture.mail import MailHelper


class Application:

    def __init__(self, browser, config):
        if browser == 'chrome':
            self.wd = webdriver.Chrome(executable_path=r'C:\gecko\chromedriver1.exe')
        elif browser == 'firefox':
            self.wd = webdriver.Firefox()
        else:
            raise ValueError('unrecognized browser')

        self.config = config
        self.base_url = config['web']['baseUrl']
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.signup = SigupHelper(self)
        self.soap = SoapHelper(self)
        self.mail = MailHelper(self)

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
