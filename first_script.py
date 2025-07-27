from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
    input_first_name.send_keys('German')
    time.sleep(5)

    input_last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
    input_last_name.send_keys('Gorozhankin')
    time.sleep(5)

    input_email = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
    input_email.send_keys('email@mail.com')
    time.sleep(5)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "Congratulations! You have successfully registered!")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()