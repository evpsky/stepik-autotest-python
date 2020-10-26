from selenium import webdriver

'''def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, \
        f"expected {expected_result}, got {actual_result}"

# Разница между подходами IN and FIND
s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

# Проверка текста в строке url
link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()
browser.get(link)
assert "telenor" in browser.current_url,\
    f"Wrolng link {link}"# сообщение об ошибке

full_string = str(input())
substring = str(input())'''

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string,\
        f"expected '{substring}' to be substring of '{full_string}'"
