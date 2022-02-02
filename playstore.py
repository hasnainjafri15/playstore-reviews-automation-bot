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

ratings_list = []
df_stores = pd.DataFrame(ratings_list, columns=['ratings'])
last_updated_list = []
installs_list = []
total_reviews_list = []
reviews_list = []
none = "none"
x = 0
for x in range(0,3): 
    x = x + 1
    app_link = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/div[2]/c-wiz/c-wiz/c-wiz/div/div[2]/div[{}]/c-wiz/div/div/div[2]/div/div/div[1]/div/div/div[1]/a/div".format(x))
    app_link.click()

    time.sleep(2)
    
    try:
            ratings = driver.find_element_by_class_name('BHMmbe').text
            ratings_list.append(ratings)
    except: 
            ratings_list.append(none)
    

    last_updated = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/div/main/c-wiz[3]/div[1]/div[2]/div/div[1]/span/div/span").text
    last_updated_list.append(last_updated)

    installs = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/div/main/c-wiz[3]/div[1]/div[2]/div/div[3]/span/div/span").text
    installs_list.append(installs)

    try:
        total_reviews = driver.find_element_by_xpath(
        "/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/div/div[2]/c-wiz/span/span[1]").text
        total_reviews_list.append(total_reviews)
    except:
        total_reviews_list.append(none)
        

    try:
        y = 1
        for y in range(1,3):
            y = y + 1
            reviews = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/div/main/div/div[1]/div[{}]/div/div[2]/div[2]/span[1]".format(y)).text
            reviews_list.append(reviews)
            
    except:
        reviews_list.append(none)

    

    time.sleep(3)

    driver.back()

driver.quit()

print(ratings_list)
print(reviews_list)
print(installs_list)
print(total_reviews_list)

df_stores['Reviews'] = pd.DataFrame(reviews_list)
df_stores['Installations'] = pd.DataFrame(installs_list)
df_stores['Total reveiws'] = pd.DataFrame(total_reviews_list)
