from urllib import request, parse

url = 'http://httpbin.org/post'
dict = {
    'name': 'Germey'
}

data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36')
response = request.urlopen(req)
print(response.read().decode('utf-8'))