import quopri
import re

class SigupHelper:

    def __init__(self, app):
        self.app = app

    def new_user(self, username, email, password):
        wd = self.app.wd
        wd.get('http://mantis/mantisbt-2.24.2/signup_page.php')
        wd.find_element_by_name('username').send_keys(username)
        wd.find_element_by_name('email').send_keys(email)
        wd.find_element_by_css_selector('input[type="submit"]').click()

        mail = self.app.mail.get_mail(username, password, '<admin@example.com>')
        url = self.extact_confirmation_url(mail)

        wd.get(url)
        wd.find_element_by_name('realname').send_keys(username)
        wd.find_element_by_name('password').send_keys(password)
        wd.find_element_by_name('password_confirm').send_keys(password)
        wd.find_element_by_css_selector('button[type="submit"]').click()

    def extact_confirmation_url(self, text):
        body = quopri.decodestring(text).decode('utf-8')
        return re.search('http://.*$', body, re.MULTILINE).group(0)


