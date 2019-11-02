#网络图片链接的格式:
# https://www.example.com/picture.jpg
#图片来源:国家地理网站 （不可用）
#https://www.nationalgeographic.com.cn/
import requests
import os
path = r'C:\Users\xxp\PycharmProjects\cxdm\mooc\abc.jpg'
url = 'http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg'
try:
    if not os.path.exists(path):
        r = requests.get(url)
        print(r.status_code)
        #b:写入二进制格式
        with open(path,'wb') as f:
            #r.content:文件的二进制格式
            f.write(r.content)
            f.close()
            print('下载成功')
    else:
        print('文件已存在')
except:
    print('爬去失败')