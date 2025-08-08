from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class CheckboxesPage(BasePage):

    def checkbox_dynamic(self, text): return self.wait_for_visible((By.XPATH, f"//form[@id='checkboxes']/input[following-sibling::text()[1][normalize-space() = '{text}']]"))

    def __init__(self, driver):
        super().__init__(driver)