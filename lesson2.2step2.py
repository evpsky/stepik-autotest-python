from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1").text
    print(x)
    y = browser.find_element_by_id("num2").text
    print(y)

    sum = int(x) + int(y)
    print(sum)
    sum_text = str(sum)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(sum_text)  # ищем элемент с текстом "Python"
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()