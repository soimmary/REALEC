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

    a = ['MTsy_14_1.txt', 'MTsy_16_1.txt', 'MTsy_17_1.txt', 'MTsy_17_2.txt', 'MTsy_18_1.txt', 'MTsy_18_2.txt', 'MTsy_19_1.txt', 'MTsy_19_2.txt', 'MTsy_20_1.txt', 'MTsy_20_2.txt', 'MTsy_21_1.txt', 'MTsy_21_2.txt', 'MTsy_22_1.txt', 'MTsy_22_2.txt', 'MTsy_23_1.txt', 'MTsy_23_2.txt', 'MTsy_24_1.txt', 'MTsy_24_2.txt', 'MTsy_25_1.txt', 'MTsy_25_2.txt', 'MTsy_26_1.txt', 'MTsy_26_2.txt', 'MTsy_27_1.txt', 'MTsy_27_2.txt', 'MTsy_28_1.txt', 'MTsy_28_2.txt', 'MTsy_29_1.txt', 'MTsy_29_2.txt', 'MTsy_30_1.txt', 'MTsy_30_2.txt', 'MTsy_31_1.txt', 'MTsy_31_2.txt', 'MTsy_32_1.txt', 'MTsy_32_2.txt', 'MTsy_33_1.txt', 'MTsy_33_2.txt', 'MTsy_34_1.txt', 'MTsy_34_2.txt', 'MTsy_35_1.txt', 'MTsy_35_2.txt', 'MTsy_36_1.txt', 'MTsy_36_2.txt', 'MTsy_37_1.txt', 'MTsy_37_2.txt', 'MTsy_38_1.txt', 'MTsy_38_2.txt', 'MTsy_39_1.txt', 'MTsy_39_2.txt', 'MTsy_40_1.txt', 'MTsy_40_2.txt', 'MTsy_41_1.txt', 'MTsy_41_2.txt', 'MTsy_42_1.txt', 'MTsy_42_2.txt', 'MTsy_43_1.txt', 'MTsy_43_2.txt', 'MTsy_7_2.txt', 'MTsy_8_1.txt', 'MTsy_8_2.txt', 'MTsy_9_1.txt', 'TSha_2_1.txt', 'TSha_2_2.txt', 'TSha_20_1.txt', 'TSha_20_2.txt', 'TSha_21_1.txt', 'TSha_21_2.txt', 'TSha_4_1.txt', 'TSha_4_2.txt', 'TSha_6_1.txt', 'TSha_6_2.txt', 'TSha_7_1.txt', 'TSha_7_2.txt', 'TSha_9_1.txt', 'TSha_9_2.txt', 'VKo_1_1.txt', 'VKo_1_2.txt', 'VKo_12_2.txt', 'VKo_13_2.txt', 'VKo_16_2.txt', 'VKo_17_1.txt', 'VKo_17_2.txt', 'VKo_18_2.txt', 'VKo_2_2.txt', 'VKo_20_2.txt', 'VKo_21_2.txt', 'VKo_23_1.txt', 'VKo_24_2.txt', 'VKo_25_2.txt', 'VKo_28_1.txt', 'VKo_29_2.txt', 'VKo_3_2.txt', 'VKo_32_1.txt', 'VKo_33_1.txt', 'VKo_33_2.txt', 'VKo_34_2.txt', 'VKo_4_2.txt', 'VKo_6_1.txt', 'VKo_7_1.txt', 'VKo_9_2.txt', 'VPe_12_1.txt', 'VPe_12_2.txt', 'VPe_17_1.txt', 'VPe_17_2.txt', 'VPe_18_1.txt', 'VPe_18_2.txt', 'VPe_19_1.txt', 'VPe_19_2.txt', 'VPe_20_1.txt', 'VPe_20_2.txt', 'VPe_21_1.txt', 'VPe_21_2.txt', 'VPe_22_1.txt', 'VPe_22_2.txt', 'VPe_23_1.txt', 'VPe_23_2.txt', 'VPe_24_1.txt', 'VPe_24_2.txt', 'VPe_25_1.txt', 'VPe_25_2.txt', 'VPe_26_1.txt', 'VPe_26_2.txt', 'VPe_27_1.txt', 'VPe_27_2.txt', 'VPe_28_1.txt', 'VPe_28_2.txt', 'VPe_30_1.txt', 'VPe_30_2.txt', 'VPe_31_1.txt', 'VPe_31_2.txt', 'VPe_32_1.txt', 'VPe_32_2.txt', 'VPe_33_1.txt', 'VPe_33_2.txt', 'VPe_34_2.txt', 'VPe_35_1.txt', 'VPe_35_2.txt', 'VPe_36_1.txt', 'AAl_14_2.txt', 'KKo_24_1.txt']

    #for path in tqdm(os.listdir(folder_path)):
    for path in tqdm(a):
        with open('grammarly_results.csv', 'a') as csvf:
            writer = csv.writer(csvf, delimiter=',')
            with open(folder_path + '/' + path, 'r') as f:
                text = f.read()
                time.sleep(3)
                insert_text = driver.find_element_by_xpath("//div[@class='_9c5f1d66-denali-editor-editor ql-editor ql-blank']").send_keys(text)
                time.sleep(15)
                score = int(driver.find_element_by_xpath("//div[@class='fhsusol _bec19051-header-performanceScoreFadeIn _48adf116-header-performanceScore']").text)
                '''if score in range(0, 6):
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
                    level = 'C2'''
                start_again = driver.find_element_by_xpath('//div[@class="_9c5f1d66-denali-editor-editor ql-editor"]').clear()
                writer.writerow([path, score])
            csvf.close()


get_level('REALEC_texts')
