from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
cap = {
    "platformName": "Android",
    "platformVersion": "4.4.2",
    "deviceName": "192.168.99.102",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "noReset": True,
    "unicodekeyboard":True,
    "resetkeyboard":True,
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",cap)
def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['width']
    return (x,y)

#点击搜索
#//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/aa9']
try:
    if WebDriverWait(driver,10).until(lambda  x:x.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/aa9']")):
        driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/aa9']").click()
except:
    pass

# #点击文本框，输入数据
# #//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a3j']
#//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/q6']
if WebDriverWait(driver,10).until(lambda  x:x.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/q6']")):
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a3j']").click()
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a3j']").send_keys("王者荣耀")
    while driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a3j']").text != "王者荣耀":
        driver.find_element_by_xpath(
            "//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/q6']").send_keys("王者荣耀")
        time.sleep(0.1)

# # 点击搜索
# # "//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/a3l']"
#//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/a3l']
# if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
#         "//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/a3l']")):
#     driver.find_element_by_xpath(
#         "//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/a3l']").click()


# l = get_size()
#
# x1 = int(l[0]*0.5)
# y1 = int(l[1]*0.75)
# y2 = int(l[1]*0.25)
# while True:
#     driver.swipe(x1,y1,x1,y2,500)
#     time.sleep(1)
