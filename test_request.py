import requests
# import json
# import re
#
data = {
    'name': 'germery',
    'age': 22
}
headers = {
    'Cookie': '_zap=a06d9e8f-08af-4e78-ad39-39c31d50ed93; d_c0="AGDoGS6JaQ6PTnGUIcSM3zjmk4a8cj4P9JY=|1540380560"; q_c1=1f68018c3ed4431480daa268518a8309|1540380563000|1540380563000; _xsrf=6hNfNzQPJbfU1byV1S2fLRcxThOzLbPW; capsion_ticket="2|1:0|10:1540733380|14:capsion_ticket|44:OGNmNjU2ZjQ4ZWU3NGJhZWFhODlkYzVlNWY1MDQ3YTY=|3bf42a63005dd03634466a0a1f5bb53ceb5559f0f0be282f50b0d9963900b066"; z_c0="2|1:0|10:1540733406|4:z_c0|92:Mi4xb2t3MkNBQUFBQUFBWU9nWkxvbHBEaVlBQUFCZ0FsVk4zZ2ZEWEFBVzc0bjNyUTB1bHpPa1ZfeF84LVUya1J6OUR3|f5ead945a9dc4e51cf919cf9db485c4e01413dfec118deec4deb911730ab6382"; tst=r; __utma=51854390.1977080788.1540733482.1540733482.1540733482.1; __utmb=51854390.0.10.1540733482; __utmc=51854390; __utmz=51854390.1540733482.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/292121532; __utmv=51854390.100--|2=registration_date=20180315=1^3=entry_date=20180315=1; tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Host': 'www.zhihu.com'
}
# response = requests.get('http://www.zhihu.com/explore', headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, response.text)
# print(titles)

files = {'file': open('favicon.ico', 'rb')}
r = requests.post('https://www.zhihu.com', headers=headers)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)
print(r.text)
print(r.history)
