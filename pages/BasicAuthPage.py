from pages.BasePage import BasePage

class BasicAuth(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_basic_auth_form(self, username="admin", password="admin"):
        url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        self.driver.get(url)