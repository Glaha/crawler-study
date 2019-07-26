import urllib.request
import http.cookiejar

'''
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Connection": "keep-alive"
'''

'''
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
'''

def userAgentOpener(head = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Connection": "keep-alive"
}):
    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

    headers = []
    for key, value in head.items():
        header = (key,value)
        headers.append(header)

    opener.addheaders = headers

    return opener

def saveFile(data):
    save_path = 'C:\work\git\python\crawler-study\save-http-responce.log'
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()
        

openTool = userAgentOpener()
uop = openTool.open("https://www.baidu.com", timeout= 1000)
data = uop.read()
saveFile(data)
print(data.decode())
