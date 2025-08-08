from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)