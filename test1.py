import urllib.parse
import urllib.request
import urllib.error
import socket


url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Host': 'httpbin.org'
}

dict = {
    'name': 'Germey'
}
data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
try:
    req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
    response = urllib.request.urlopen(req)
    print(type(response))
    print(response.status)
    print(response.getheaders())
    print(response.getheader('Server'))
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
