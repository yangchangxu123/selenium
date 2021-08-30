from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

wd = webdriver.Chrome()
wd.maximize_window()
wd.get('http://www.baidu.com')
setting = wd.find_element('id','s-usersetting-top')
ActionChains(wd).move_to_element(setting).perform()
sleep(3)
wd.find_element_by_link_text('高级搜索').click()
sleep(2)
#截图
wd.save_screenshot('2.png')
