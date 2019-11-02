import requests
import re
search = input('请输入你想要下载的图片类型')
url = 'https://image.baidu.com/search/flip?tn=baiduimage&word={search}'

html = requests.get(url).text
# print(html)
image_urls = re.findall('"objURL":"(.*?)"',html,)
# print(image_urls)
for image in image_urls:
    # print(image)
    image_na = image.split('/')[-1]
    image_name = re.search('.jpg|.jpeg|.bmp|.png|.gif|.tif',image_na)
    if image_name == None:
        image_na = image_na + '.jpg'
    print(image_na)
    content = requests.get(image).content
    with open('./image/%s'%image_na,'wb') as f:
        f.write(content)