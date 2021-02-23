import random
import string
from idlelib import browser
from _pytest.mark import param
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class New_ProjectPage(object):
    def  __init__(self,browser):
        self.browser = browser

    def get_random_string(self, length):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def add(self,name):
        name_field = self.browser.find_element_by_id('name')
        prefix_field = self.browser.find_element_by_id('prefix')
        description_field = self.browser.find_element_by_css_selector('textarea')
        save_button = self.browser.find_element_by_id('save')
        name_field.send_keys(name)
        prefix_field.send_keys(self.get_random_string(3))
        description_field.send_keys(self.get_random_string(3))
        save_button.click()

    def verify_project_added(self):
        wait = WebDriverWait(self.browser, 15)
        info_add = (By.ID, 'j_info_box')
        wait.until(expected_conditions.visibility_of_element_located(info_add))





