from selenium import webdriver


class Test_window:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
    def test_window(self):
        self.driver.find_element(By.XPATH,())
    def teardaown(self):
        pass