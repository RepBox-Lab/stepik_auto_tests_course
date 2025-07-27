from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import os


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('German')

    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Gorozhankin')

    e_mail = browser.find_element(By.NAME, 'email')
    e_mail.send_keys('german@gmail.com')
 
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')
    download_file = browser.find_element(By.NAME, 'file')
    download_file.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()