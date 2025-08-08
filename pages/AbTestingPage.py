from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class AbTestingPage(BasePage):

    def header_dynamic(self, tag="h3"): return self.wait_for_visible((By.XPATH, f"//{tag}"))

    def __init__(self, driver):
        super().__init__(driver)