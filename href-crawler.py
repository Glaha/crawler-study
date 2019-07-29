import urllib.request as request
import re
import urllib
from collections import deque

url = "http://www.baidu.com/"
queue = deque()
queue.append(url)

visited = set()

count = 0
while queue:
    url = queue.popleft()
    print("fetching url:" + url)
    count += 1
    visited |= {url}
    
    try:
        urlop = request.urlopen(url)
        if 'html' not in urlop.getheader('Content-Type'):
            continue
        data = urlop.read().decode('utf-8')
    except:
        continue
    
    ex = re.compile('href="(.+?)"')     
    
    for x in ex.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
