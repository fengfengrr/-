from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By



class Testtouch:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)


    def test_touch(self):
        self.driver.get('http://www.baidu.com')
        el = self.driver.find_element(By.XPATH,('//*[@id="kw"]'))
        el_search = self.driver.find_element(By.XPATH,('//*[@id="su"]'))
        el.send_keys('我是你爸爸')
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()
        action.scroll(0,10000).perform()
        eltext = self.driver.find_element_by_xpath('//*[@id="page"]/a[8]/span[2]')
        action.tap(eltext).perform()


