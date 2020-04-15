from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest


class Test_click:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def test_click(self):
        dbl = self.driver.find_element(By.XPATH ('//*[@name="f1"]/input[2]'))
        dblclick = ActionChains(dbl)
        dblclick.double_click()
        dblclick.perform()
if __name__ == '__main__':
    pytest.main(['-v','-s','test.py'])
