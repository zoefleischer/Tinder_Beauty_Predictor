# ----------------------Tinder Login Selenium----------------------------------------

import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars --disable-extensions --window-size=4000,4000")


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options=options)

    def login(self):
        self.driver.get('https://tinder.com')
        time.sleep(1)
        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        time.sleep(1)
        login_btn.click()
        time.sleep(3)
        fb_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        time.sleep(1)
        fb_btn.click()
        time.sleep(1)
        base_window = self.driver.window_handles[0]
        time.sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[1])
        time.sleep(1)
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        time.sleep(1)
        email_in.send_keys('joaoquintela0@gmail.com')
        time.sleep(1)
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        time.sleep(1)
        pw_in.send_keys('Vporctf69.')
        time.sleep(1)
        login = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login.click()
        time.sleep(2)
        self.driver.switch_to_window(base_window)
        time.sleep(2)
        location_allow = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        time.sleep(2)
        location_allow.click()
        time.sleep(1)
        enable = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        time.sleep(2)
        enable.click()
        time.sleep(2)
