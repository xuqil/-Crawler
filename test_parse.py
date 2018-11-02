from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html', scheme='https')
print(type(result), result)