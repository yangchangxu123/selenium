from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


#启动Firefox浏览器
#Browser_FireFox = webdriver.Firefox()
#启动Chrome浏览器
Browser_Chrome = webdriver.Chrome()

#窗口最大化
Browser_Chrome.maximize_window()
#打开网址
Browser_Chrome.get('https://www.gogbuy.com/')
#获取页面标题
print(Browser_Chrome.title)
print(Browser_Chrome.current_url)


# Browser_FireFox.find_element('name','keyword').send_keys('测试')
# Browser_FireFox.find_element_by_xpath('//*[@class = "search po_re"]/button').click()

#设置显示等待，找到优惠券就进行下一步
WebDriverWait(Browser_Chrome,10,0.5).until(lambda e1:Browser_Chrome.find_element_by_link_text('优惠券'))
#点击跳转到优惠券页面
Browser_Chrome.find_element_by_link_text('优惠券').click()
#点击跳转到文创贵州页面
Browser_Chrome.find_element_by_link_text('文创贵州').click()

#获取浏览器所有句柄
handles = Browser_Chrome.window_handles
handle1 = Browser_Chrome.current_window_handle
print(handles)
#遍历所有句柄
for handle in handles:
    #切换句柄
    Browser_Chrome.switch_to.window(handle)
    try:
        Browser_Chrome.find_element('id','//*[@id="myTab0_Content0"]/ul/li[2]')
        print(handle)
        print('切换到领取页面')
        break
    except:
        pass

WebDriverWait(Browser_Chrome,10,0.5).until(lambda e1:Browser_Chrome.find_element_by_xpath('//*[@id="myTab0_Content0"]/ul/li[2]'))
Browser_Chrome.find_element('xpath','//*[@id="myTab0_Content0"]/ul/li[2]').click()
Browser_Chrome.switch_to.window(handle1)

sleep(3)
Browser_Chrome.quit()