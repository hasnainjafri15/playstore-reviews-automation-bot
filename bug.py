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

output = pd.DataFrame()


app_link = driver.find_element_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/c-wiz/c-wiz/c-wiz/div/div[2]/div[{}]/c-wiz/div/div/div[2]/div/div/div[1]/div/div/div[1]/a/div'.format(2))
app_link.click()

time.sleep(5)

reviews = driver.find_element_by_xpath(
    '/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/div/main/div/div[1]/div[#2]/div/div[2]/div[2]/span[1]').text
print(reviews)


#/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/div/main/div/div[1]/div[3]/div/div[2]/div[2]/span[1]
#/html/body/div[1]/div[4]/c-wiz[2]/div/div[2]/div/div/main/div/div[1]/div[2]/div/div[2]/div[2]/span[1]
