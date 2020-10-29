from selenium import webdriver
import time
import math


def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    browser.get(link)
    button = browser.find_element_by_css_selector(".btn")
    button.click()
    alert = browser.switch_to_alert()
    alert.accept()
    value_count = browser.find_element_by_id("input_value").text
    print(value_count)
    count = int(value_count)
    print(count)
    number = calc(count)
    print(number)
    number_str = str(number)
    name = browser.find_element_by_name("text")
    name.send_keys(number_str)
    button_submit = browser.find_element_by_css_selector(".btn")
    button_submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

