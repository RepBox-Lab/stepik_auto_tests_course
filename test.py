from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '.form-group .nowrap#input_value')
    x = x_element.text
    y = calc(x)

    input_math = browser.find_element(By.CSS_SELECTOR, '.form-control#answer')
    input_math.send_keys(y)

    submint = browser.find_element(By.CSS_SELECTOR, '.btn-primary.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submint)
    button_not_robot = browser.find_element(By.CSS_SELECTOR, '.form-check-input#robotCheckbox').click()
    radiobuttion_robots_rule = browser.find_element(By.CSS_SELECTOR, '.form-check-input#robotsRule').click()
    submint.click()
    time.sleep(4)
finally:
    browser.quit()
