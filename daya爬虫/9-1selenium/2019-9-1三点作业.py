from selenium import webdriver
import time
import json

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

#-----------------------1
# #获取cookie
# cookies = browser.get_cookies()
# print(cookies)
#
# #删除所有cookie信息
# browser.delete_all_cookies()
# #循环重新写入
# for cookie in cookies:
#     # print(cookie)
#     browser.add_cookie(cookie)
# #刷新
# browser.refresh()
# print('ready')
#
# time.sleep(3)

#----------------------2----在headers中添加cookie信息


#------------------------测试

input = browser.find_element_by_id('q')
input.send_keys('python')
time.sleep(3)
input.clear()
time.sleep(3)
input.send_keys('Python')
button = browser.find_element_by_class_name('btn-search')#找到按钮
button.click()

browser.refresh()

browser.find_element_by_id("J_Quick2Static").click()

browser.refresh()
time.sleep(3)
# browser.find_element_by_id("TPL_username_1").send_keys("tb87651580")
# browser.find_element_by_id("TPL_password_1").send_keys("41632543xxp")
# browser.find_element_by_id("TPL_username_1").click()
browser.find_element_by_id("J_SubmitStatic").click()