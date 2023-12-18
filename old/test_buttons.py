import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base_url import BASE_URL
from selenium import webdriver

import locators

class Test_Buttons_Menu():

    def test_setup(self):
        global driver, actionChains
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(BASE_URL)
        actionChains = ActionChains(driver)

    def test_open_elements_page(self):
        elements_menu = driver.find_element(By.XPATH, locators.ELEMENTS_MENU_LOCATOR)
        elements_menu.click()

    def test_open_buttons_page(self):
        driver.execute_script("window.scrollTo(0, 100)")
        buttons_click = driver.find_element(By.ID, locators.BUTTONS_CLICK_ID)
        buttons_click.click()

    def test_double_click(self):
        double_click_button = driver.find_element(By.XPATH, locators.DOUBLE_CLICK_BUTTON_LOCATOR)
        actionChains.double_click(double_click_button).perform()

    def test_right_click(self):
        right_click_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
        actionChains.context_click(right_click_button).perform()

    def test_dynamic_click(self):
        click_me_button = driver.find_element(By.XPATH, "//button[text()='Click Me']")
        click_me_button.click()



