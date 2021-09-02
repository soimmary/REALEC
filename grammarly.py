from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from tqdm import tqdm
import time
import os
import csv

import personal_info

LOGIN = personal_info.LOGIN
PASSWORD = personal_info.PASSWORD

'''
0-5   - A1
6-10  - A2
11-20 - В1-
21-30 - В1
31-40 - В1+
41-50 - В2
51-60 - В2+
61-70 - С1
71+   - С2
'''


def calculate_level(x):
    if x in range(0, 6):
        return 'A1'
    elif x in range(6, 11):
        return 'A2'
    elif x in range(11, 41):
        return 'B1'
    elif x in range(41, 51):
        return 'B2'
    elif x in range(51, 71):
        return 'C1'
    elif x in range(71, 101):
        return 'C2'


def recalculate_level(x):
    if x in range(0, 6):
        return 'A1'
    elif x in range(6, 11):
        return 'A2'
    elif x in range(11, 21):
        return 'B1-'
    elif x in range(21, 31):
        return 'B1'
    elif x in range(31, 41):
        return 'B1+'
    elif x in range(41, 51):
        return 'B2'
    elif x in range(51, 61):
        return 'B2+'
    elif x in range(61, 71):
        return 'C1'
    elif x in range(71, 101):
        return 'C2'


def get_level(folder_path):
    global LOGIN, PASSWORD
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Firefox(executable_path=r'/Users/mariabocharova/PycharmProjects/REALEC/firefoxdriver')
    driver.get('https://www.grammarly.com/signin')

    insert_email = driver.find_element_by_name('email').send_keys(LOGIN)
    continue_btn = driver.find_element_by_xpath("//button[@class='base_basic__1qybc base_colorGreen__2AdOl']").click()
    time.sleep(5)

    insert_password = driver.find_element_by_name('password').send_keys(PASSWORD)
    sign_in = driver.find_element_by_xpath("//button[@class='base_basic__1qybc base_colorGreen__2AdOl']").click()
    time.sleep(5)

    open_new_file = driver.find_element_by_xpath("//div[@data-name='new-doc-add-btn']").click()
    time.sleep(5)

    for path in tqdm(os.listdir(folder_path)):
        with open('grammarly_results.csv', 'a') as csvf:
            writer = csv.writer(csvf, delimiter=',')
            with open(folder_path + '/' + path, 'r') as f:
                text = f.read()
                time.sleep(3)
                insert_text = driver.find_element_by_xpath(
                    "//div[@class='_9c5f1d66-denali-editor-editor ql-editor ql-blank']").send_keys(text)
                time.sleep(10)
                score = int(driver.find_element_by_xpath(
                    "//div[@class='fhsusol _bec19051-header-performanceScoreFadeIn _48adf116-header-performanceScore']"
                ).text)
                level = calculate_level(score)
                recalc_level = recalculate_level(score)
                writer.writerow([folder_path.split('/')[-1] + '/' + path, level, recalc_level])
                start_again = driver.find_element_by_xpath(
                    '//div[@class="_9c5f1d66-denali-editor-editor ql-editor"]'
                ).clear()
            csvf.close()


# the absolute path to the folder
folder = '/Users/mariabocharova/PycharmProjects/REALEC/REALEC_texts'
get_level(folder)
