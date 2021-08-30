#等待界面元素出现
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class  TestCase():
    def __init__(self):
        self.wd = webdriver.Chrome()
        #self.wd.implicitly_wait(10)


    def test_baidu(self):
        self.wd.get('https://www.baidu.com')
        element = self.wd.find_element_by_id('kw')

        element.send_keys('白月黑羽\n')

        # id 为 1 的元素 就是第一个搜索结果
        element = self.wd.find_element_by_id('1')

        # 打印出 第一个搜索结果的文本字符串
        print(element.text)

    def test_selenium_alert(self):
        self.wd.get('https://www.selenium.dev/zh-cn/documentation/webdriver/js_alerts_prompts_and_confirmations/')
        # Click the link to activate the alert
        self.wd.find_element(By.LINK_TEXT, "查看样例警告框").click()
        wait = WebDriverWait(self.wd,10)
        # Wait for the alert to be displayed and store it in a variable
        alert = wait.until(expected_conditions.alert_is_present())
        # Store the alert text in a variable
        text = alert.text
        print(text)
        # Press the OK button
        alert.accept()

    def test_selenium_confirm(self):
        self.wd.get('https://www.selenium.dev/zh-cn/documentation/webdriver/js_alerts_prompts_and_confirmations/')
        # Click the link to activate the alert
        self.wd.find_element(By.LINK_TEXT, "查看样例确认框").click()
        wait = WebDriverWait(self.wd,10)
        # Wait for the alert to be displayed and store it in a variable
        wait.until(expected_conditions.alert_is_present())
        # Store the alert text in a variable
        alert = self.wd.switch_to.alert
        text = alert.text
        print(text)
        # Press the OK button
        #点击确认按钮
        # alert.accept()
        #点击取消按钮
        alert.dismiss()

if __name__ == '__main__':
    # TestCase().test_selenium_alert()
    TestCase().test_selenium_confirm()