import json
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Test_cookies:
    def setup(self):
        option = webdriver.ChromeOptions()
        #引入chrome环境变量
        option.debugger_address='127.0.0.1:9222'
        #设置chromedebug地址
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)
    def test_cookie(self):
        sleep(3)
        #第一次获取cookies，外界登陆，获取cookies，并储存到cookies.txt
        # cookies = self.driver.get_cookies()
        # with open('cookies.txt','w') as f:
        #     json.dump(cookies,f)

        with open('cookies.txt','r' ) as f:
            #读取cookies.txt
            cookies:List[Dict] = json.load(f)
            for cookie in cookies:
                #遍历cookies 用selenium读取cookie
                if 'expiry' in cookie.keys():
                    #运行时出错，无法识别变量expiry，故删除
                    cookie.pop('expiry')
                self.driver.add_cookie(cookie)
            self.driver.get('https://work.weixin.qq.com/')
            self.driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
            self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_item_title').click()
            self.driver.find_element(By.ID,'username').send_keys('bjmasefbhjwea')
            self.driver.find_element(By.XPATH,('//*[@id="memberAdd_acctid"]')).send_keys('wudi')
            self.driver.find_element(By.CSS_SELECTOR,'.ww_radio').click()
            self.driver.find_element(By.XPATH,'//*[@id="js_contacts36"]/div/div[2]/div/div[4]/div/form/div[3]/a[1]').click()


