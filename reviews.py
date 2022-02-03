from ast import Break, Return
from asyncio.windows_events import NULL
from functools import total_ordering
from gettext import install
import re
from webbrowser import Chrome
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://play.google.com/store/apps/developer?id=Blink+Co.")

time.sleep(22)

none = [0,0,0,0,0]

df_price = pd.DataFrame()

x = 0
while x in range(3):
    reviews_list = []
    x = x + 1
    try:
        app_link = driver.find_element_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/c-wiz/c-wiz/c-wiz/div/div[2]/div[{}]/c-wiz/div/div/div[2]/div/div/div[1]/div/div/div[1]/a/div'.format(x))
        app_link.click()
    except:
        pass

    time.sleep(2)

    #name = driver.find_element_by_class_name('AHFaub').text

    list = [2, 3, 4, 5, 6]

    for y in list:
           #y = y + 1
           #print(x)
           #time.sleep(2)
           #print(y)
           #driver.execute_script("window.scrollBy(0,3000)", "")
            try:
                reviews = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/div/main/div/div[1]/div[{}]/div/div[2]/div[2]/span[1]'.format(y)).text
                reviews_list.append(reviews)
            except:
                reviews_list.append('N/A')

    driver.back()
    time.sleep(2)

    df_price[x] = pd.DataFrame(reviews_list)
    df_price['sentiment'] = none


driver.quit()


df_price