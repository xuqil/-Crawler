import re
import requests

content = requests.get('https://docs.pythontab.com/').text
pattern = re.compile('<h3.*?text-left">(.*?)</h3>', re.S)
result = re.findall(pattern, content)
for res in result:
    print(res)
# print(result)
