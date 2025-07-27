from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value.nowrap')
    x = x_element.text
    y = calc(x)
    input_math = browser.find_element(By.CSS_SELECTOR, '.form-group .form-control')
    input_math.send_keys(y)
    time.sleep(5)
    
    checkbox_i_am_robot = browser.find_element(By.CSS_SELECTOR, '.form-check.form-check-custom .form-check-input#robotCheckbox')
    checkbox_i_am_robot.click()
    time.sleep(5)

    radiobutton_robots = browser.find_element(By.CSS_SELECTOR, '.form-check.form-radio-custom .form-check-input#robotsRule')
    radiobutton_robots.click()
    time.sleep(5)

    button_submit = browser.find_element(By.CSS_SELECTOR, '.btn-default.btn')
    button_submit.click()
    time.sleep(5)

finally:
    time.sleep(30)
    browser.quit()

