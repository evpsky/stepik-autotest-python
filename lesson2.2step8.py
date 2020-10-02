from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #Ищем число
    x = browser.find_element_by_id("input_value").text
    print(x)
    x2 = int(x)
    print(x2)
    # Считаем функцию
    y = calc(x2)
    print(y)
    # Скроллим к кнопке

    # Ввоидм ответ на функцию
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)
    # Выбираем чекбокс
    robot = browser.find_element_by_css_selector("#robotCheckbox")
    robot.click()
    # Выбираем радиобаттон
    rule = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rule)
    rule.click()
    # Кикаем сабмит
    button = browser.find_element_by_css_selector(".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()