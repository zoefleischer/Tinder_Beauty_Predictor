
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars --disable-extensions --window-size=4000,4000")


    # ---------------------------SCRAPING THE PICTURES----------------------

    def get_pics(self):
        self.driver.execute_script("document.body.style.zoom='1%'")
        time.sleep(2)
        elem_1 = self.driver.find_elements_by_xpath(
            '//div[@class="D(f) Flw(w)"]')  # ("//div[@class='Whs(nw) Pt(4px) Pb(12px) Px(8px) NetHeight(100%,50px) W(100%) Trsp(a)! Trsdu($normal) Pos(a) Ovy(s) Ovs(touch) Ovx(h) Ovsby(n)']/div/div/a/div")
        time.sleep(1)
        elem_each = [el.find_elements_by_xpath('//div[@class="P(8px) Ta(c)"]') for el in elem_1]

        time.sleep(1)
        elem_all = [el.find_elements_by_xpath('//a/div[@class="recCard__img StretchedBox Bdrs(4px) P(4px)"]')
                    for elem in elem_each for el in elem]
        time.sleep(1)

        self.pics = [el.get_attribute('style').replace('background-image: url("', '') \
                         .replace('"); background-position: 50% 50%; background-size: auto 100%;', '') \
                         .replace('320x400', '640x800').replace('320x320', '640x640')
                     for elem in elem_all for el in elem]

        time.sleep(2)
        return self.pics


tb = TinderBot()
link = tb.login()
pics = tb.get_pics()
tb.driver.close()


#----------------------DOWNLOADING THE PICS---------------

#extracting only the url
pics = [el.replace('; background-position: 50% 50%; background-size: auto 125%;','')
          .replace('")','')
          .replace('"); background-position: 50% 48.3871%; background-size: auto 108.401%;','') for el in pics]

#looping through the url list and saving to jpg on PC

import urllib.request

i=0
pics = list(set(pics))
for url in pics:
    urllib.request.urlretrieve(url, str(i)+'.jpg')
    i+=1