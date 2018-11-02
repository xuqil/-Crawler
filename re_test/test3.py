import re
import requests

content = requests.get('https://book.douban.com/').text
with open('text.txt', 'w', encoding='utf-8') as f:
    f.write(content)
# print(content)
# pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
pattern = re.compile('<li.*?cover.*?title="(.*?)">.*?</a>', re.S)
result = re.findall(pattern, content)
for res in result:
    print(res)
# print(result)