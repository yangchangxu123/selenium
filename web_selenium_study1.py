#练习
from selenium import webdriver
#创建启动Chrome示例
wd = webdriver.Chrome(r"d:\python\chromedriver.exe")
wd.implicitly_wait(5)
#窗口最大化
wd.maximize_window()
#在打开浏览器中，输入访问链接
wd.get("http://127.0.0.1/mgr/sign.html")
#定位到账号输入框
username = wd.find_element_by_id('username')
#定位到密码输入框
password = wd.find_element_by_id('password')
#输入账号
username.send_keys('byhy')
#输入/密码
password.send_keys('88888888')
#定位登陆按钮
login_button = wd.find_element_by_class_name('btn')#btn btn-primary btn-block btn-flat  一共有4个class元素，取其中一个即可
#点击登陆按钮
login_button.click()
#限制 选择元素的范围是 class 为 col-lg-12 元素的内部。
add =  wd.find_element_by_class_name('col-lg-12')
#在从add内部中，再定位tag为button标签的元素
add.find_element_by_tag_name('button').click()

print(username.get_attribute('outerHTML'))