from selenium.webdriver.common.by import By
from selenium import webdriver
from base_url import BASE_URL

driver = webdriver.Firefox()
driver.get(BASE_URL)

elements_menu = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[1]")
elements_menu.click()

checkbox = driver.find_element(By.XPATH, "//*[@id='item-1']")
checkbox.click()

home_toggle = driver.find_element(By.XPATH, "//*[@id='tree-node']/ol/li/span/button")
home_toggle.click()

downloads_toggle = driver.find_element(By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[3]/span/button")
downloads_toggle.click()

checkbox_word_file = driver.find_element(By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[3]/ol/li[1]/span/label/span[3]")
checkbox_word_file.click()

check_text = driver.find_element(By.XPATH,"//*[@id='result']/span[2]")
assert check_text.text, "wordFile"

driver.implicitly_wait(10)
driver.quit()