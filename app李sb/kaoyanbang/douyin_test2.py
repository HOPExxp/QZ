from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
cap = {
    "platformName": "Android",
    "platformVersion": "4.4.2",
    "deviceName": "192.168.99.102：62001",
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
try:
    if WebDriverWait(driver,10).until(lambda  x:x.find_element_by_id("com.ss.android.ugc.aweme:id/aa9")):
        driver.find_element_by_id("com.ss.android.ugc.aweme:id/aa9").click()
except:
    pass
#点击文本框，输入数据
#//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a3j']
if WebDriverWait(driver,10).until(lambda  x:x.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a3j']")):
    # driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a3j']").click()
    driver.tap([(360,70),(400,60)],100)
    driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a3j']").send_keys("王者荣耀")
    while driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/a3j']").text != "王者荣耀":
        driver.find_element_by_xpath(
            "//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/q6']").send_keys("王者荣耀")
        time.sleep(0.1)


#点击搜索
#"//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/a3l']"
if WebDriverWait(driver,10).until(lambda  x:x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/a3l']")):
    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/a3l']").click()

#点击用户
if WebDriverWait(driver,10).until(lambda  x:x.find_element_by_xpath("//android.widget.FrameLayout/android.widget.TextView[4]")):
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.TextView[4]").click()

#查看是否有关注
if WebDriverWait(driver,10).until(lambda  x:x.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.ss.android.ugc.aweme:id/kf']/android.widget.RelativeLayout[1]")):
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.ss.android.ugc.aweme:id/kf']/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
