import datetime
import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.buttons_page import ButtonsPage
from pages.checkbox_page import CheckboxPage
from tests.conftest import browser

class TestSuitElementsPage():

    def test_buttons_page(self, browser):
        buttons_page = ButtonsPage(driver=browser)
        buttons_page.click_open_elements_page()
        logging.info('open_buttons_page')
        buttons_page.click_open_buttons_page()
        logging.info('double_click')
        buttons_page.click_double_click_btn()
        logging.info('right_click')
        buttons_page.click_right_click()
        logging.info('dynamic_click')
        buttons_page.click_dynamic_click()

    def test_checkbox_page(self, browser):
        checkbox_page = CheckboxPage(driver=browser)
        logging.info('click_open_checkbox_page')
        checkbox_page.click_open_checkbox_page()
        logging.info('click_home_toggle')
        checkbox_page.click_home_toggle()
        logging.info('downloads_toggle')
        checkbox_page.click_downloads_toggle()
        logging.info('checkbox_word_file')
        checkbox_page.click_checkbox_word_file()
        logging.info('check_text_success')
        checkbox_page.put_check_text_success()
        table_page = browser.find_element(By.ID, "item-3")
        table_page.click()
        table = WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='rt-tr-group']/div/div[3]")))
        logging.info(table[1].text)



    def test_slider(self, browser):
        logging.info("close_elements")
        close_elements = browser.find_element(By.XPATH, "//div[@class='header-right']")
        close_elements.click()
        browser.execute_script("window.scrollTo(0, 300)")
        logging.info("widgets_page")
        widgets_page = browser.find_elements(By.XPATH, "//div[@class='header-wrapper']")
        widgets_page[3].click()
        action = ActionChains(browser)
        logging.info("slider_button_click")
        slider_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".accordion>.element-group:nth-child(4) #item-3")))
        slider_button.click()
        logging.info("click_and_hold(slider)")
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_click_and_hold(slider)' + now_date + '.png'
        slider = browser.find_element(By.XPATH,"//div[@class='col-9']")
        action.click_and_hold(slider).move_by_offset(100, 0).release().perform()
        browser.save_screenshot(name_screenshot)

    def test_table(self):
        pass



