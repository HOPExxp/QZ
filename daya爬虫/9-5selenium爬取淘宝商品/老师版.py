"""
成功获取一页的全部数据
"""


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException  # 异常处理模块
import time
from pymongo import MongoClient
from pyquery import PyQuery as pq

client = MongoClient()
db = client.taobao
yurongfu = db.yurongfu
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)


def search():
    try:
        driver.get('https://www.taobao.com')
        input = wait.until(EC.presence_of_element_located((By.ID, 'q')))  # 获取搜索框
        # 获取搜索按钮
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        input.send_keys(u'阿迪达斯')  # 加u表示转换编码格式
        submit.click()
        # 等待页面加载完成
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        return total.text
    except TimeoutException:
        return search()


def next_page(page_number):
    try:
        # 找到翻页输入框
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form >input')))
        # 找到确定按钮
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form >span.btn.J_Submit')))
        input.clear()  # 由于翻页框中有数字需要先清除
        input.send_keys(page_number)
        submit.click()
        # text_to_be_presence_in_element等待条件，某节点包含某文字，意思是输入number在这个节点中，即可
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div >div >ul >li.item.active > span'), str(page_number)))
    except TimeoutException:
        next_page(page_number)


def get_products():
    # 等待item节点加载完成
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist > div > div > div > div.item')))
    html = driver.page_source  # 获取源码
    doc = pq(html)  # pq解析
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': 'https' + item.find('.pic .img').attr('src'),  # 获取图片链接
            'price': item.find('.price').text(),  # 获取价格
            'deal': item.find('.deal-cnt').text(),  # 获取购买人数
            'title': item.find('.title').text(),  # 获取标题
            'shop': item.find('.shop').text(),  # 获取店名
            'location': item.find('.location').text()  # 获取店的位置
        }
        print(product)
        yurongfu.insert(product)


def main():
    search()
    for page_number in range(1, 3):  # 如果要爬取多页自己设置数量在100内
        next_page(page_number)
        get_products()


if __name__ == '__main__':
    main()