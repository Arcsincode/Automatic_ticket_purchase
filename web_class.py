from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium import webdriver
import os
import json
import pandas as pd
from datetime import datetime
import csv
import random
import threading
import queue
import re
import time
# from lib.file_op import csv_op
import queue
from abc import ABC

class a_web(ABC):
    def __init__(self,wait_time=20,lang='zh',gui=True):
        options = webdriver.ChromeOptions()
        path="/usr/bin/chromedriver"
        options.add_argument("--no-sandbox")
        if not gui:
            options.add_argument("--headless")
            options.add_argument('--disable-gpu')
        if lang=='en':
            options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(executable_path=path,options=options)
        self.driver.set_window_size(1200, 800)
        self.wait = WebDriverWait(self.driver, wait_time)

    def get(self,url,long_flag=False):
        while True:
            try:
                self.driver.get(url)
                break
            except Exception as e:
                if long_flag:
                    print("获取网页失败")
                    continue
                else:
                    raise e
        

    def wait_find(self,by=By.ID,value="email",long_flag=False,change_wait_to=-1,find_all=False):
        if not change_wait_to == -1:
            wait=WebDriverWait(self.driver, change_wait_to)
        else:
            wait=self.wait
        if long_flag:
            while True:
                try:
                    wait.until(ec.presence_of_element_located((by, value)))
                    break
                except:
                    pass
        else:
            wait.until(ec.presence_of_element_located((by, value)))
        if find_all:
            return self.driver.find_elements(by,value) 
        else:
            return self.driver.find_element(by,value)

