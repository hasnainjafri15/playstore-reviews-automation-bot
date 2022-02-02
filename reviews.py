from ast import Break, Return
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

reviews_list = []


x = 0
for x in range(0,3): 
    x = x + 1
    app_link = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/div[2]/c-wiz/c-wiz/c-wiz/div/div[2]/div[{}]/c-wiz/div/div/div[2]/div/div/div[1]/div/div/div[1]/a/div".format(x))
    app_link.click()

    time.sleep(2)

    #name = driver.find_element_by_xpath(
        #'/html/body/div[1]/div[4]/c-wiz[3]/div/div[2]/div/div/main/c-wiz/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1/span').text
    

    try:
        y = 1
        for y in range(1,3):
            y = y + 1
            reviews = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/div/main/div/div[1]/div[{}]/div/div[2]/div[2]/span[1]".format(y)).text
            name = []  #name should be that of name
            name.append(reviews)
            r_r = pd.DataFrame(name, columns=[name])
            
    except:
        reviews_list.append('none')

    time.sleep(2)

    driver.back()

driver.quit()

print(r_r)

