import os
import csv
import time

from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

import personal_info


LOGIN = personal_info.LOGIN
PASSWORD = personal_info.PASSWORD


def get_level(folder_path, my_wb_path, my_essay_path):
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
    my_wb = driver.find_element_by_xpath(my_wb_path).click()
    time.sleep(2)
    my_essay = driver.find_element_by_id(my_essay_path).click()
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
                    time.sleep(15)
                    level = driver.find_element_by_xpath('//*[@id="scroller"]/main/div/div/section[1]'
                                                         '/div/header/div[2]/div/div/p[2]').text
                    writer.writerow([folder_path.split('/')[-1] + '/' + path, level])
                    # time.sleep(5)
                except Exception as e:
                    print(e)
                    continue
            csvf.close()


# the absolute path to the folder
folder = '/Users/mariabocharova/PycharmProjects/REALEC/REALEC_texts'
my_wb_path = 'your workbook path'
my_essay_path = 'your essay path'
get_level(folder, my_wb_path, my_essay_path)
