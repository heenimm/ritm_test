from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
from base.base_class import Base
from base.base_url import BASE_URL


class Buttons_page(Base):
    url = BASE_URL

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_elements_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locators.ELEMENTS_MENU_LOCATOR)))

    def get_buttons_click(self):
        return self.driver.find_element(By.ID, locators.BUTTONS_CLICK_ID)

    def get_double_click_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locators.DOUBLE_CLICK_BUTTON_LOCATOR)))

    def get_right_click_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locators.RIGHT_CLICK_BUTTON_LOCATOR)))

    def get_dynamic_click_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locators.CLICK_ME_BUTTON_LOCATOR)))


    def click_open_elements_page(self):
        elements_menu = self.get_elements_menu()
        elements_menu.click()


    def click_open_buttons_page(self):
        self.driver.execute_script("window.scrollTo(0, 100)")
        elements_menu = self.get_buttons_click()
        elements_menu.click()

    def click_double_click_btn(self):
        actionChains = ActionChains(self.driver)
        actionChains.double_click(self.get_double_click_button()).perform()

    def click_right_click(self):
        actionChains = ActionChains(self.driver)
        actionChains.context_click(self.get_right_click_button()).perform()

    def click_dynamic_click(self):
        self.get_dynamic_click_button().click()
