from selenium import webdriver
import time


dict_browsers = {
    'firefox': './geckodriver.exe',
    'chrome': './chromedriver.exe',
}

for name, path_browser in dict_browsers.items():
    lines = list()
    browser = ''
    if name == 'firefox':
        browser = webdriver.Firefox(executable_path=f'{path_browser}')
    elif name == 'chrome':
        browser = webdriver.Chrome(f'{path_browser}')

    with open('signup-accounts-{}.csv'.format(name), mode='r') as f:
        lines = f.readlines()
        f.close()

    for i in lines:
        acc = i.strip('\n').split(',')
        username = acc[0]
        email = acc[1]

        browser.get("http://127.0.0.1/mantisbt/signup_page.php")
        time.sleep(3)
        user_input = browser.find_element_by_id("username")
        user_input.send_keys(username)

        email_input = browser.find_element_by_id("email-field")
        email_input.send_keys(email)

        button = browser.find_element_by_css_selector(
            "input.width-40.pull-right.btn.btn-success.btn-inverse.bigger-110")
        button.submit()
    browser.close()
