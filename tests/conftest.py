import  pytest
from selenium import webdriver

from pages.BasicAuthPage import BasicAuth
from pages.BrokenImagePage import BrokenImagePage
from pages.MainPage import MainPage
from pages.AbTestingPage import AbTestingPage
from pages.AddRemoveElementsPage import AddRemoveElements
from pages.CheckboxesPage import CheckboxesPage


@pytest.fixture(scope="session")
def chrome():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

    driver = webdriver.Chrome(options=options)
    #driver.get("https://the-internet.herokuapp.com/")
    yield driver
    driver.close()
    driver.quit()

@pytest.fixture(scope="function")
def main_page(chrome):
    chrome.get("https://the-internet.herokuapp.com/")
    return MainPage(chrome)

@pytest.fixture(scope="function")
def ab_testing_page(chrome):
    return AbTestingPage(chrome)

@pytest.fixture(scope="function")
def add_remove_elements_page(chrome):
    return AddRemoveElements(chrome)

@pytest.fixture(scope="function")
def basic_auth_page(chrome):
    return BasicAuth(chrome)

@pytest.fixture(scope="function")
def broken_image_page(chrome):
    return BrokenImagePage(chrome)

@pytest.fixture(scope="function")
def checkboxes_page(chrome):
    return CheckboxesPage(chrome)




