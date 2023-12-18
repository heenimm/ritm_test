import time

import pytest
from base_url import BASE_URL
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.get(BASE_URL)
    yield browser
    time.sleep(10)
    browser.quit()
