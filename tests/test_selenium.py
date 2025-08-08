from time import sleep

import  pytest
from selenium import webdriver
from selenium.webdriver.common.devtools.v136.runtime import await_promise

class TestSelenium:

    def test_ab_testing(self, main_page, ab_testing_page):
        assert main_page.header_dynamic("Welcome to the-internet").is_displayed()
        main_page.link_dynamic("A/B Testing").click()
        assert ab_testing_page.header_dynamic().text in ["A/B Test Variation 1", "A/B Test Control"]

    def test_add_remove_element(self, main_page, add_remove_elements_page):
        assert main_page.header_dynamic("Welcome to the-internet").is_displayed()
        main_page.link_dynamic("Add/Remove Elements").click()
        assert add_remove_elements_page.header_dynamic("Add/Remove Elements", "h3").is_displayed()
        add_remove_elements_page.button_dynamic("Add Element").click()
        add_remove_elements_page.button_dynamic("Add Element").click()
        assert add_remove_elements_page.number_of_elements(add_remove_elements_page.list_of_elements_dynamic("Delete", "button")) == 2
        add_remove_elements_page.click_each_element(add_remove_elements_page.list_of_elements_dynamic("Delete", "button"))
        assert add_remove_elements_page.number_of_elements(add_remove_elements_page.list_of_elements_dynamic("Delete", "button")) == 0

    def test_basic_auth(self, main_page, basic_auth_page):
        assert main_page.header_dynamic("Welcome to the-internet").is_displayed()
        main_page.link_dynamic("Basic Auth").click()
        basic_auth_page.fill_basic_auth_form("admin", "admin")
        assert basic_auth_page.header_dynamic("Basic Auth", "h3").is_displayed()
        assert basic_auth_page.text_dynamic("Congratulations! You must have the proper credentials.", "p").is_displayed()

    def test_broken_images(self, main_page, broken_image_page):
        assert main_page.header_dynamic("Welcome to the-internet").is_displayed()
        main_page.link_dynamic("Broken Images").click()
        assert broken_image_page.header_dynamic("Broken Images", "h3").is_displayed()
        assert len(broken_image_page.get_broken_images()) != 0

    def test_checkboxes(self, main_page, checkboxes_page):
        assert main_page.header_dynamic("Welcome to the-internet").is_displayed()
        main_page.link_dynamic("Checkboxes").click()
        assert checkboxes_page.header_dynamic("Checkboxes", "h3").is_displayed()
        checkboxes_page.checkbox_dynamic("checkbox 1").click()
        assert checkboxes_page.checkbox_dynamic("checkbox 1").get_attribute("checked") == "true"
        assert checkboxes_page.checkbox_dynamic("checkbox 2").get_attribute("checked") == "true"
        checkboxes_page.checkbox_dynamic("checkbox 1").click()
        checkboxes_page.checkbox_dynamic("checkbox 2").click()
        assert checkboxes_page.checkbox_dynamic("checkbox 1").get_attribute("checked") is None
        assert checkboxes_page.checkbox_dynamic("checkbox 2").get_attribute("checked") is None


