"""Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)


    price = WebDriverWait(browser, 13).until(
        text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    button = browser.find_element(By.ID, 'book')
    button.click()

    input_value = browser.find_element(By.ID, 'input_value')
    x = input_value.text
    y = calc(x)

    math_answer = browser.find_element(By.ID, 'answer')
    math_answer.send_keys(y)

    button_submit = browser.find_element(By.ID, 'solve')
    button_submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    time.sleep(5)

finally:
    browser.quit()
    #
