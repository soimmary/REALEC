import os
import csv
import time

from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

import personal_info_wi


LOGIN = personal_info.LOGIN_WI
PASSWORD = personal_info.PASSWORD_WI


def get_level(folder_path):
    global LOGIN, PASSWORD
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(options=options,
                              executable_path=r'/Users/mariabocharova/PycharmProjects/REALEC/chromedriver')
    driver.get('https://writeandimprove.com/workbooks?login=sign-in')

    # insert an email and a password
    time.sleep(3)
    insert_email = driver.find_element_by_id('email-or-username').send_keys(LOGIN)
    time.sleep(2)
    insert_password = driver.find_element_by_id('password').send_keys(PASSWORD)
    continue_ = driver.find_element_by_id('btn-sign-in').click()
    time.sleep(5)
    my_wb = driver.find_element_by_xpath('//*[@id="sidebar-workbook-60bca5b8-96f8-4cba-9b78-d12fb18a61c5"]/a').click()
    time.sleep(2)
    my_essay = driver.find_element_by_id('task-60bd05a9-212c-408b-a440-403df000a998').click()
    time.sleep(1)

    for path in tqdm(os.listdir(folder_path)):
        with open('write_improve_results.csv', 'a') as csvf:
            writer = csv.writer(csvf, delimiter=',')
            with open(folder_path + '/' + path, 'r') as f:
                text = f.read()
                try:
                    start_again = driver.find_element_by_xpath('//*[@id="scroller"]/main/div/section[2]'
                                                               '/section/div/div/div[2]/main/a[1]').click()
                    insert_text = driver.find_element_by_xpath('//textarea').send_keys(text)
                    insert_text = driver.find_element_by_xpath('//textarea').send_keys(' ')
                    time.sleep(2)
                    check = driver.find_element_by_id('check').click()
                    time.sleep(10)
                    level = driver.find_element_by_xpath('//*[@id="scroller"]/main/div/div/section[1]'
                                                         '/div/header/div[2]/div/div/p[2]').text
                    writer.writerow([path, level])
                except Exception as e:
                    print(e)
                    continue
            csvf.close()


get_level('/PycharmProjects/REALEC/REALEC_texts')
