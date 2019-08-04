import requests
from bs4 import BeautifulSoup

def getTokenByRegex(html):
    soup = BeautifulSoup(html,features="html.parser")
    x = soup.find("input", {"name": "authenticity_token"})['value']
    print(x)
    return x

def getTokenFromGithub(head):
    resp = requests.get("https://github.com/login",headers=head,verify=False)
    html = resp.text
    print(resp.cookies)
    return getTokenByRegex(html),resp.cookies

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
    "Upgrade-Insecure-Requests":"1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
}


def login(username, password,token, head, cookies):
    postDict = {
        "commit":"Sign in",
        "utf8": "✓",
        "authenticity_token": token,
        "login": username,
        "password": password,
        "webauthn-support": "supported"
    }
    resp = requests.post("https://github.com/session",data=postDict, headers=head,verify=False, cookies=cookies)
    print(resp.text)
    return resp.text

token, cookies_login = getTokenFromGithub(head_get_token)
login("Glaha", "xxxxxxx", token, head_login, cookies_login)
