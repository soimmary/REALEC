import os
import time
import csv
from tqdm import tqdm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


chromedriver_path = '/Users/mariabocharova/PycharmProjects/REALEC/chromedriver'


def get_level(folder_path):
    global chromedriver_path
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(options=options, executable_path=chromedriver_path)
    driver.get('https://cefr.duolingo.com/')

    for path in tqdm(os.listdir(folder_path)):
        with open('duolingo_results.csv', 'a') as csvf:
            writer = csv.writer(csvf, delimiter=',')
            with open(folder_path + '/' + path, 'r', encoding='utf-8') as f:
                text = f.read()
                try:
                    clear_text = driver.find_element_by_xpath("//textarea[@class='_1c55K']").clear()
                    insert_text = driver.find_element_by_xpath("//textarea[@class='_1c55K']").send_keys(text)
                    time.sleep(5)
                    level = driver.find_element_by_xpath("//div[@class='RZxzk']").text
                    writer.writerow([folder_path.split('/')[-1] + '/' + path, level])
                    time.sleep(2)
                except Exception as e:
                    print(e)
                    continue
            csvf.close()
    driver.close()

# absolute path to the folder
folder = '/Users/mariabocharova/PycharmProjects/REALEC/REALEC_texts'
get_level(folder)
