from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser,10)
#     wait.until(EC.presence_of_all_elements_located(By.ID,'content_left'))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

# browser.get('https://taobao.com')
# #查找单个节点
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first)
# print(input_second)
# print(input_third)
# #查找多个节点  注意element多了一个s
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)

# #节点交互 -- 单个节点
# #输入文字
# input_first.send_keys('iphone')
# #清空文字
# sleep(3)
# input_first.clear()
# #搜索功能
# input_first.send_keys('ipad')
# sleep(3)
# button = browser.find_element_by_class_name('btn-search')
# button.click()
# sleep(3)

# #动作链 -- 多个节点
# from selenium.webdriver import ActionChains
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')#切换到iframe中
# source = browser.find_element_by_css_selector('#draggable')#找到拖拽节点
# target = browser.find_element_by_css_selector('#droppable')#找到目标节点
# #声明动作链的对象
# actions = ActionChains(browser)
# actions.drag_and_drop(source,target)#drag_and_drop动作链
# actions.perform()#执行

#执行JavaScript
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,2000)')
# browser.execute_script('alert("0,2000")')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert(document.body.scrollHeight)')

#7.切换Frame
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# browser.switch_to.frame('iframeResult')#切换到iframe中
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()#切换到父级frame用parent_frame（）方法
# logo = browser.find_element_by_class_name('logo')
# print(logo.text)

#8.延时等待
#隐式等待 -- 没获取最多等待10秒，默认为0秒
# browser.implicitly_wait(0.1)
# browser.get('https://www.zhihu.com/explore')

# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)
# a = browser.find_element_by_xpath('//li/a[@href="//www.zhihu.com/"]')
# print(a.text)

#显式等待
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser,10)
# buttom = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
# input = wait.until(EC.presence_of_element_located((By.ID,'q')))
# print(input,buttom)

#9.前进和后退
# browser.get('https://www.baidu.com')
# sleep(3)
# browser.get('https://www.taobao.com')
# sleep(3)
# browser.get('https://www.zhihu.com')
# sleep(3)
# browser.back()
# sleep(3)
# browser.forward()
# sleep(3)
# browser.close()

# 10.cookies
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name':'xxp','value':'18','domain':'www.zhihu.com'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

#11.选项卡管理
# browser.get('https://www.baidu.com')
# sleep(3)
# browser.execute_script('window.open()')
# sleep(3)
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[0])
# sleep(3)
# browser.get('https://www.taobao.com')
# sleep(3)
# browser.switch_to_window(browser.window_handles[1])
# sleep(3)
# browser.get('https://www.zhihu.com')

#12.异常处理


# print(browser.page_source)
