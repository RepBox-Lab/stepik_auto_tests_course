from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import os
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/alert_accept.html')
    button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value.nowrap')
    x = x_element.text
    y = calc(x)
    form_to = browser.find_element(By.CLASS_NAME, 'form-control')
    form_to.send_keys(y)
    form_to2 = browser.find_element(By.CLASS_NAME, 'btn-primary')
    form_to2.click()
    time.sleep(5)


finally:

    time.sleep(5)
    browser.quit()