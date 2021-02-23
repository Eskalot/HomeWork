
class Projects_View_Page():
    def  __init__(self,browser):
        self.browser = browser


    def search(self,name):
        search_bar = self.browser.find_element_by_id('search')
        button = self.browser.find_element_by_id('j_searchButton')
        search_bar.send_keys(name)
        button.click()

    def verify_project_found(self,name):
        project = self.browser.find_element_by_link_text(name)
        assert project.is_displayed() is True


