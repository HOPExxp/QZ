import urllib
import urllib.request
import http.cookiejar

loginURL = 'http://120.55.151.61:80/V2/StudentSkip/loginCheckV4.action'
ListURL = "http://120.55.151.61:80/Treehole/V4/Message/getListByType.action"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 -SuperFriday_9.4.0',
    'Host': '120.55.151.61:80',
    'Connection': "Keep-Alive",
    'Accept-Encoding': 'gzip',
    'Content-Length': "285"
}

loginData = {"password": "fe14",
             "account": "9edd",
             "registrationId": "",
             "ifa": "5606A9A6-",
             "ifv": "F277A23",
             "versionNumber": "9.4.0",
             "platform": "2",
             "channel": "AppStore",
             "phoneVersion": "11.3",
             "phoneModel": "iPhone%208",
             "phoneBrand": "Apple"}
data = bytes(urllib.parse.urlencode(loginData), encoding='utf8')
cookieJar = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookieJar)
opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)
data = urllib.request.urlopen(loginURL, data)
print(data.read())

requestData = {"type": 1,
               "timestamp": 0,
               "versionNumber": "9.4.0",
               "platform": 2,
               "channel": "AppStore",
               "phoneVersion": "11.3",
               "phoneModel": "iPhone%208",
               "phoneBrand": "Apple"}
byteData = bytes(urllib.parse.urlencode(requestData), encoding='utf8')
urllib.request.install_opener(opener)
data = urllib.request.urlopen(ListURL, byteData)
print(data.read().decode('utf-8'))
