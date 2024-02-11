from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')

input_elements = driver.find_element(By.CLASS_NAME, 'gLFyf')
input_elements.clear()
input_elements.send_keys('tech with tim' + Keys.RETURN)

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf')))

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Tech with tim')))

link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Tech with tim')
link.click()

time.sleep(10)
driver.quit()