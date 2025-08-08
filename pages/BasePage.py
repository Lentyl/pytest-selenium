from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def header_dynamic(self, text, tag="h1"): return self.wait_for_visible((By.XPATH, f"//{tag}[normalize-space()='{text}']"))
    def text_dynamic(self, text, tag="p"): return self.wait_for_visible((By.XPATH, f"//{tag}[normalize-space()='{text}']"))
    def button_dynamic(self, text, tag="button"): return self.wait_for_visible((By.XPATH, f"//{tag}[normalize-space()='{text}']"))
    def link_dynamic(self, text, tag="a"): return self.wait_for_visible((By.XPATH, f"//{tag}[normalize-space()='{text}']"))

    def list_of_elements_dynamic(self, text, tag="a"):  return self.driver.find_elements(*(By.XPATH, f"//{tag}[normalize-space()='{text}']"))



    def wait_for_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def number_of_elements(elements: list[WebElement]) -> int:
        return len(elements)

    @staticmethod
    def click_each_element(elements: list[WebElement]):
        for el in elements:
            el.click()



