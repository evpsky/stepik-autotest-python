import pytest
from selenium import webdriver
import time
import math





@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url',
                         ["236895", "236896", "236897", "236899", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, url):
    answer = str(math.log(int(time.time() + 4)))

    link = f"https://stepik.org/lesson/{url}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    text_field = browser.find_element_by_css_selector(".textarea")
    text_field.send_keys(answer)
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    time.sleep(5)
    answ_comment_elt = browser.find_element_by_css_selector(".smart-hints__hint")
    answ_comment = answ_comment_elt.text
    print(answ_comment)
    assert "Correct!" == answ_comment