import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from pages.testarena_login_page import LoginPage
from pages.test_arena_add_project_page import New_ProjectPage
from pages.testarena_logged_page import TestArena
from pages.testarena_projects_view_page import Projects_View_Page


@pytest.fixture()
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('http://demo.testarena.pl/zaloguj')
    yield browser
    browser.quit()

def test_create_project(browser):
# zaloguj do TestArena
    login_page = LoginPage(browser)
    login_page.login()

# przejdz do panelu administracyjnego
    testarena = TestArena(browser)
    testarena.wait_for_load()
    testarena.click_a_panel()

#przejdz do dodawania projektu
    new_project_page = New_ProjectPage(browser)
    random_project_name = new_project_page.get_random_string(15)
    #added_project = random_project_name
    new_project_page.add(random_project_name)
    new_project_page.verify_project_added()
#przejdz do strony z widokiem projektów
   

#wyszukaj dodany projekt
    browser.get('http://demo.testarena.pl/administration/projects')
    projects_view_page = Projects_View_Page(browser)
    projects_view_page.search(random_project_name)
    projects_view_page.verify_project_found(random_project_name)

















