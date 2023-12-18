from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import locators
from base.base_class import Base
from base_url import BASE_URL


class Checkbox_page(Base):
    url = BASE_URL

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_checkbox_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, locators.CHECKBOX_CLICK_ID)))

    def get_home_toggle_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locators.HOME_TOGGLE_LOCATOR)))

    def get_downloads_toggle_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locators.DOWNLOAD_TOGGLE_LOCATOR)))

    def get_checkbox_word_file_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locators.CHECKBOX_WORD_FILE)))

    def get_check_text_success_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locators.CHECK_TEXT_SUCCESS)))

    def click_open_checkbox_page(self):
        checkbox_page = self.get_checkbox_locator()
        checkbox_page.click()

    def click_home_toggle(self):
        home_toggle = self.get_home_toggle_locator()
        home_toggle.click()

    def click_downloads_toggle(self):
        downloads_toggle = self.get_downloads_toggle_locator()
        downloads_toggle.click()

    def click_checkbox_word_file(self):
        checkbox_word_file = self.get_checkbox_word_file_locator()
        checkbox_word_file.click()

    def put_check_text_success(self):
        check_text_success = self.get_check_text_success_locator()
        assert check_text_success.text, "wordFile"

