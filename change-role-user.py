from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

dict_browsers = {
    'firefox': './geckodriver.exe',
    'chrome': './chromedriver.exe',
}

for name, path_browser in dict_browsers.items():
    lines = list()
    browser = None
    if name == 'firefox':
        browser = webdriver.Firefox(executable_path=f'{path_browser}')
    elif name == 'chrome':
        browser = webdriver.Chrome(f'{path_browser}')

    with open('user-info-{}.csv'.format(name), mode='r') as f:
        lines = f.readlines()
        f.close()

    browser.get("http://127.0.0.1/mantisbt/login_page.php")
    user_input = browser.find_element_by_id("username")
    user_input.send_keys('admin')

    button_sb1 = browser.find_element_by_css_selector(
        "input.width-40.pull-right.btn.btn-success.btn-inverse.bigger-110")
    button_sb1.submit()
    time.sleep(5)
    pass_input = browser.find_element(By.ID, "password")
    pass_input.send_keys("admin123")
    button_sb2 = browser.find_element_by_css_selector(
        "input.width-40.pull-right.btn.btn-success.btn-inverse.bigger-110")
    button_sb2.submit()
    time.sleep(5)
    for i in lines:
        acc = i.strip('\n').split(',')
        username = acc[0]
        user_id = acc[1]
        browser.get("http://127.0.0.1/mantisbt/manage_overview_page.php")
        browser.get("http://127.0.0.1/mantisbt/manage_user_page.php")
        browser.get(
            f"http://127.0.0.1/mantisbt/manage_user_edit_page.php?user_id={user_id}")
        select = Select(browser.find_element_by_id('edit-access-level'))
        # ex: 1712882_i -> if i % 2 != 0 ? 55 : 70 (dev | manager)
        if int(username.split('_')[1]) % 2 != 0:
            select.select_by_value('55')
        else:
            select.select_by_value('70')
        if name == 'firefox':
            button_update = browser.find_element_by_xpath(
                '//input[@type="submit" and @value="Cập nhật người dùng"]')
        else:
            button_update = browser.find_element_by_xpath(
                '//input[@type="submit" and @value="Update User"]')
        button_update.click()

    browser.close()
