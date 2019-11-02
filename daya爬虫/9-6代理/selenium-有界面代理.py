from selenium import webdriver

proxy = '127.0.0.1:808'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://'+proxy)
browser = webdriver.Chrome(options=chrome_options)
browser.get('http://httpbin.org/get')