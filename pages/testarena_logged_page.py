from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class TestArena():
    def __init__(self, browser):
        self.browser = browser

    def wait_for_load(self):
        wait = WebDriverWait(self.browser, 10)
        adm_panel = (By.CLASS_NAME, 'top_right')
        wait.until(expected_conditions.visibility_of_element_located(adm_panel))


    def click_a_panel(self):
        panel = self.browser.find_element_by_css_selector("[href='http://demo.testarena.pl/administration']")
        panel.click()
        add_button = self.browser.find_element_by_css_selector("[href='http://demo.testarena.pl/administration/add_project']")
        add_button.click()
