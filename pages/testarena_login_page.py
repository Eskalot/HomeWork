
class LoginPage:
    def __init__(self, browser):
        self.browser = browser
    def login(self):
        login_field = self.browser.find_element_by_id('email')
        pswd_field = self.browser.find_element_by_id('password')
        submit_button = self.browser.find_element_by_id('login')

        login_field.send_keys('administrator@testarena.pl')
        pswd_field.send_keys('sumXQQ72$L')
        submit_button.click()


