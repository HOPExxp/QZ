from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get('http://www.taobao.com')
sleep(2)
driver.find_element_by_css_selector('a.h').click()

driver.add_cookie({'name':'userName','value':'tb87651580'})
driver.add_cookie({'name':'password','value':'41632543xxp'})

sleep(10)
driver.get('http://www.taobao.com')
driver.find_element_by_id('q').send_keys('python')
