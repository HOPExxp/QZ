import requests
import urllib.request
import urllib3
urllib3.disable_warnings()

def get_url(url):
    headers = {'user-agent': 'mobile'}
    req = requests.get(url, headers=headers, verify=False)
    data = req.json()
    for data in data['aweme_list']:
        name = data['desc'] or data['aweme_id']
        url = data['video']['play_addr']['url_list'][0]
        urllib.request.urlretrieve(url, filename=name + '.mp4')


if __name__ == "__main__":
    get_url(
        'https://www.iesdouyin.com/aweme/v1/challenge/aweme/?ch_id=1574030716416014&count=9&cursor=0&aid=1128&screen_limit=3&download_click_limit=0&_signature=XFt5MRAVAWqSMP.jPenjdVxbeS')


#https://aweme.snssdk.com/aweme/v1/challenge/aweme/?iid=30373511894&device_id=35781128184&os_api=18&app_name=aweme&channel=App%20Store&idfa=811A8841-030F-4AEA-B934-C2A56489C32D&device_platform=iphone&build_number=17805&vid=A4BB3AF4-7981-4805-995B-78419881DC11&openudid=99bf2b608173e21cefd562496d2cf21fa8eba580&device_type=iPhone7,2&app_version=1.7.8&version_code=1.7.8&os_version=11.3&screen_width=750&aid=1128&ac=WIFI&ch_id=1574030716416014&count=21&cursor=0&pull_type=2&query_type=0&type=5&mas=001469ed4a7a3f61de046e21c8c7ae8bcb64a983471da18ec0c8d1&as=a1c5206d9e676a38ee4960&ts=1524500606

#https://aweme.snssdk.com/aweme/v1/challenge/aweme/?iid=30373511894&device_id=35781128184&os_api=18&app_name=aweme&channel=App%20Store&idfa=811A8841-030F-4AEA-B934-C2A56489C32D&device_platform=iphone&build_number=17805&vid=A4BB3AF4-7981-4805-995B-78419881DC11&openudid=99bf2b608173e21cefd562496d2cf21fa8eba580&device_type=iPhone7,2&app_version=1.7.8&version_code=1.7.8&os_version=11.3&screen_width=750&aid=1128&ac=WIFI&ch_id=1574030716416014&count=21&cursor=0&pull_type=2&query_type=0&type=5&mas=001469ed4a7a3f61de046e21c8c7ae8bcb64a983471da18ec0c8d1&as=a1c5206d9e676a38ee4960&ts=1524500606

#https://aweme.snssdk.com/aweme/v1/challenge/aweme/?ch_id=1574030716416014&count=21&cursor=0&pull_type=2&query_type=0&type=5&as=a1c5206d9e676a38ee4960&ts=1524500606

#https://www.iesdouyin.com/share/challenge/1574030716416014?utm_campaign=client_share&app=aweme&utm_medium=ios&iid=30373511894&utm_source=weixin&tt_from=weixin&utm_source=weixin&utm_medium=aweme_ios&utm_campaign=client_share&uid=58875748483&did=30373511894