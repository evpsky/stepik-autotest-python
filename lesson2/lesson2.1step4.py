from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector(".form-group #input_value")
    x = x_element.text
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    button_checkbox = browser.find_element_by_css_selector(".check-input#robotCheckbox")
    button_checkbox.click()
    button_radio = browser.find_element_by_css_selector(".check-input#robotsRule")
    button_radio.click()
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()