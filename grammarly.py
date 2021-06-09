import os
import time
import csv
from tqdm import tqdm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

import personal_info


LOGIN = personal_info.LOGIN
PASSWORD = personal_info.PASSWORD


def get_level(folder_path):
    global LOGIN, PASSWORD
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Firefox(executable_path=r'/Users/mariabocharova/PycharmProjects/REALEC/firefoxdriver')
    driver.get('https://www.grammarly.com/signin')

    insert_email = driver.find_element_by_name('email').send_keys(LOGIN)
    continue_btn = driver.find_element_by_xpath("//button[@class='ZvEwE-basic _1XsA2-colorGreen']").click()
    time.sleep(3)
    insert_password = driver.find_element_by_name('password').send_keys(PASSWORD)
    sign_in = driver.find_element_by_xpath("//button[@data-qa='btnLogin']"
                                           "[@class='ZvEwE-basic _1XsA2-colorGreen']").click()
    time.sleep(7)
    open_new_file = driver.find_element_by_xpath("//div[@data-name='new-doc-add-btn']").click()
    time.sleep(2)

    for path in tqdm(os.listdir(folder_path)):
        with open('grammarly_results.csv', 'a') as csvf:
            writer = csv.writer(csvf, delimiter=',')
            with open(folder_path + '/' + path, 'r') as f:
                text = f.read()
                time.sleep(3)
                insert_text = driver.find_element_by_xpath("//div[@class='_9c5f1d66-denali-editor-editor ql-editor ql-blank']").send_keys(text)
                time.sleep(15)
                score = int(driver.find_element_by_xpath("//div[@class='fhsusol _bec19051-header-performanceScoreFadeIn _48adf116-header-performanceScore']").text)
                if score in range(0, 6):
                    level = 'A1'
                elif score in range(6, 11):
                    level = 'A2'
                elif score in range(11, 41):
                    level = 'B1'
                elif score in range(41, 51):
                    level = 'B2'
                elif score in range(51, 71):
                    level = 'C1'
                elif score in range(71, 101):
                    level = 'C2'
                start_again = driver.find_element_by_xpath('//div[@class="_9c5f1d66-denali-editor-editor ql-editor"]').clear()
                writer.writerow([path, level, score])
            csvf.close()


get_level('/PycharmProjects/REALEC/REALEC_texts')
