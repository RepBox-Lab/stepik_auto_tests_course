from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/selects1.html')

    find_style_90x = browser.find_element(By.CSS_SELECTOR, '.container')
    find_action = browser.find_element(By.TAG_NAME, 'form')
    find_h2 = browser.find_element(By.TAG_NAME, 'h2')
    find_num_1 = browser.find_element(By.CSS_SELECTOR, '.nowrap#num1')
    x = find_num_1.text
    find_num_2 = browser.find_element(By.CSS_SELECTOR, '.nowrap#num2')
    y = find_num_2.text
    sum = (int(x) + int(y))
    print(sum)


    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(sum))

    find_button = browser.find_element(By.CSS_SELECTOR, '.btn-default.btn')
    find_button.click()


finally:
    time.sleep(5)
    browser.quit()

