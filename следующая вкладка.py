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
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button_trolface = browser.find_element(By.CSS_SELECTOR, '.trollface')
    button_trolface.click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(5)

    find_x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = find_x.text
    y = calc(x)

    input_num = browser.find_element(By.CSS_SELECTOR, '.form-control')
    input_num.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    submit.click()
    time.sleep(2)

finally:
    browser.quit()

    # обновление