from pages.buttons_page import Buttons_page
from pages.checkbox_page import Checkbox_page
from tests.conftest import browser

class Test_suit_elements_page():

    def test_buttons_page(self, browser):
        buttons_page = Buttons_page(driver=browser)
        buttons_page.click_open_elements_page()

        print('open_buttons_page')
        buttons_page.click_open_buttons_page()
        print('double_click')
        buttons_page.click_double_click_btn()
        print('right_click')
        buttons_page.click_right_click()
        print('dynamic_click')
        buttons_page.click_dynamic_click()

    def test_checkbox_page(self, browser):
        checkbox_page = Checkbox_page(driver=browser)

        print('click_open_checkbox_page')
        checkbox_page.click_open_checkbox_page()
        print('click_home_toggle')
        checkbox_page.click_home_toggle()
        print('downloads_toggle')
        checkbox_page.click_downloads_toggle()
        print('checkbox_word_file')
        checkbox_page.click_checkbox_word_file()
        print('check_text_success')
        checkbox_page.put_check_text_success()


