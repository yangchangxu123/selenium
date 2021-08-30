import time

from selenium import webdriver

wd = webdriver.Chrome(r'D:\python\chromedriver.exe')    #启动浏览器驱动(也就是打开一个浏览器),Chrome  是一个类，这里实例化

wd.maximize_window()
wd.get("http://cdn1.python3.vip/files/selenium/sample1.html") #输入url

# element = wd.find_element_by_id('kw')
# element =element.send_keys('白月黑羽')


class_name = wd.find_element_by_class_name("plant")  #element不加s的话，只获取多个属性中的第一个。
print(class_name.text)
class_name = wd.find_elements_by_class_name("plant") #获取的是一个list，需要对这个数组遍历
for i in class_name:
    print(i.text)
print("\t")
tag_name = wd.find_element_by_tag_name("div")
print(tag_name.text)
tag_name = wd.find_elements_by_tag_name("div")
# for j in tag_name:
#     print(j.text)


#公共webelement选择元素
element = wd.find_element_by_id("container")  # 限制 选择元素的范围是 id 为 container 元素的内部。
element_ele = element.find_elements_by_tag_name("span")
for x in element_ele:
    print(x.text)


time.sleep(3)
wd.quit()