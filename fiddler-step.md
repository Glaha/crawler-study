# Steps for all programs's crawler

## Catalogs

- [Steps for all programs's crawler](#steps-for-all-programss-crawler)
  - [Catalogs](#catalogs)
  - [Use fiddler monitor requests](#use-fiddler-monitor-requests)
  - [Mock the requests by code](#mock-the-requests-by-code)

## Use fiddler monitor requests

- Make sure fiddler is capturing requests. F12
- Use SwitchySharp/Omega to proxy requests by fiddler monitoring port 8888. 127.0.0.1
- Then you can visit the website you want.

## Mock the requests by code

- Notify that the headers are all covered
  1. Cookies should not miss
  2. User-Agent should be replaced with your own browsers
  3. Accept/Accept-Language/Content-Type almost used in many statement
  4. Referer can be used for some websites , but not certainly needed
  5. If Accept-Encoding is using gzip, pls unzip response
- Body should has the token in security way
