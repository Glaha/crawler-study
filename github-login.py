import re
import urllib.request
import urllib.parse
import http.cookiejar
import gzip

def ungzip(data):
    try:
        print("expressing")
        data = gzip.decompress(data)
        print("finish express")
    except :
        print("no compress")
    return data

def getTokenByRegex(html):
    regex = re.compile("(?<=name\=\"authenticity_token\" value=\").*(?=\" />)")
    for x in regex.findall(html):
        print(x)
        return x

# getTokenByRegex(' <form class="home-hero-signup js-signup-form" autocomplete="off" aria-label="Sign up" action="/join" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="1st9nb8zxD+ChumUUiXuO7XUo9F37zBN44fJR5wXz75YW81JmhxmyHbdiFLrF5UbUMeujkg1lYbzHZkeOdnWOQ==" />        <div class="d-lg-flex flex-wrap flex-lg-nowrap flex-justify-between">')

def buildHeader(opener, head):
    headers = []
    for key, value in head.items():
        header = (key,value)
        headers.append(header)

    opener.addheaders = headers
    return opener

def getOpener(head):
    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

    buildHeader(opener, head)

    return opener

# curl -X GET https://github.com
# opener = getOpener(head)
def getTokenFromGithub(head, opener):
    op = opener.open("https://github.com/login")
    html = op.read().decode()
    return getTokenByRegex(html)

# getTokenFromGithub(head=head_common)

def login(username, password,token, head, opener):
    #token = getTokenFromGithub(head, opener)
    postDict = {
        "commit":"Sign in",
        "utf8": "✓",
        "authenticity_token": token,
        "login": username,
        "password": password,
        "webauthn-support": "supported"
    }
    postData = urllib.parse.urlencode(postDict).encode()
    op = opener.open("https://github.com/session",postData)
    readData = op.read()
    html = readData.decode()
    print(html)
    return html

head_get_token = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Connection": "Keep-Alive"
}

head_login = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    # "Accept-Encoding": "gzip, deflate, br", # 如果有用 gzip , 必须进行解压才能获得响应内容
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",

    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "github.com",
    "Origin": "https://github.com",
    "Referer": "https://github.com/login",
    "Upgrade-Insecure-Requests":1,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
}
opener = getOpener(head_get_token)
token = getTokenFromGithub(head_get_token, opener)
opener = buildHeader(opener, head_login)
login("Glaha", "csljh2017", token, head_login, opener)
