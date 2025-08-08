from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class AbTestingPage(BasePage):

    HEADER = (By.XPATH, "//h3")

    def __init__(self, driver):
        super().__init__(driver)