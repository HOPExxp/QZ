from selenium import webdriver
service_args = [
    '--proxy=127.0.0.1:808',
    '--proxy-type=http',
    # 需要认证时加上这行
    # '--proxy-auth=username:password'
]
browser = webdriver.PhantomJS(service_args=service_args,executable_path=r"C:\Users\xxp\PycharmProjects\cxdm\venv\Scripts\phantomjs.exe")
browser.get('http://httpbin.org/get')
print(browser.page_source)