from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
cap = {
  "platformName": "Android",
  "platformVersion": "4.4.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",cap)
def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['width']
    return (x,y)


#判断是否有跳过界面，并实现跳过操作
try:
    if WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']")):
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']").click()
except:
    pass

#完成登陆操作
try:
    if WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']")):
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']").send_keys('hopexxp')
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_password_edittext']"
          ).send_keys('41632543xxp')
        driver.find_element_by_xpath(
          "//android.widget.Button[@resource-id='com.tal.kaoyan:id/login_login_btn']").click()
except:
    pass

# #点击研训操作0
# if WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//android.view.View[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]")):
#     driver.find_element_by_xpath("//android.view.View[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]").click()

#点击研训操作

if WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//android.view.View[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]")):
    driver.find_element_by_xpath(
    "//android.view.View[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()

# 点击搜索
# "//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/a3l']"
if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/a3l']")):
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/a3l']").click()

    # l = get_size()
    #
    # x1 = int(l[0]*0.5)
    # y1 = int(l[1]*0.75)
    # y2 = int(l[1]*0.25)
    # while True:
    #     driver.swipe(x1,y1,x1,y2,500)
    #     time.sleep(1)


