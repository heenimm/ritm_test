import time

import pytest

from base_url import BASE_URL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HOME_TOGGLE_LOCATOR, DOWNLOAD_TOGGLE_LOCATOR, ELEMENTS_MENU_LOCATOR, CHECKBOX_WORD_FILE, \
    CHECK_TEXT_SUCCESS

class Test_Checkbox_Menu():
    @pytest.fixture(scope="module")
    def setup(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(BASE_URL)
        yield
        time.sleep(50)
        driver.quit()


    def test_open(self, setup):
        elements_menu = driver.find_element(By.XPATH, ELEMENTS_MENU_LOCATOR)
        elements_menu.click()
        checkbox = driver.find_element(By.ID, "item-1")
        checkbox.click()


    def test_check(self, setup):
        home_toggle = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, HOME_TOGGLE_LOCATOR)))
        home_toggle.click()
        downloads_toggle = driver.find_element(By.XPATH, DOWNLOAD_TOGGLE_LOCATOR)
        downloads_toggle.click()
        checkbox_word_file = driver.find_element(By.XPATH,CHECKBOX_WORD_FILE)
        checkbox_word_file.click()
        check_text_success = driver.find_element(By.XPATH, CHECK_TEXT_SUCCESS)
        assert check_text_success.text, "wordFile"