from selenium import webdriver
import time
import math
import time


def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # get link
    browser.get(link)
    # find needed button
    button = browser.find_element_by_css_selector(".btn")
    button.click()
    # find new tab in browser
    time.sleep(2)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # find value for calculations + calculations
    value_count = browser.find_element_by_id("input_value").text
    print(value_count)
    count = int(value_count)
    print(count)
    number = calc(count)
    print(number)
    number_str = str(number)
    # find text field and send the calculated value
    name = browser.find_element_by_name("text")
    name.send_keys(number_str)
    # find and clock submit button
    button_submit = browser.find_element_by_css_selector(".btn")
    button_submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

