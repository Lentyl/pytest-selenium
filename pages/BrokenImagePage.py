from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class BrokenImagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_broken_images(self):
        images = self.driver.find_elements(By.TAG_NAME, "img")
        broken = []
        for img in images:
            result = self.driver.execute_script("return arguments[0].naturalWidth", img)
            if result == 0:
                broken.append(img.get_attribute("src"))
                print(img.get_attribute("src"), "broken")
        return broken