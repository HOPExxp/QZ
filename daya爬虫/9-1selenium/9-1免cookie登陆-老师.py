from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json


browser = webdriver.Chrome()
browser.get('https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F')
WebDriverWait(browser,30)
cookies = browser.get_cookies()
with open('cookie.json','w',encoding='utf-8') as f:
    r = f.write(json.dumps(cookies))
##    data = json.loads(str(r))
##    print(data)
wait = WebDriverWait(browser,30)
wait.until(EC.presence_of_element_located((By.ID,'q')))
browser.get('https://www.taobao.com')
browser.delete_all_cookies()
with open('cookie.json','r') as f:
    t = f.read()
    items = json.loads(t)
    for index,item in enumerate(items):
        if item:
            browser.add_cookie(item)
            print(item)
            time.sleep(1)
time.sleep(5)
browser.get('https://www.taobao.com')
##print(browser.get_cookies())
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(5)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()