from bs4 import BeautifulSoup


with open('text.txt', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
result = soup.find_all('h4')
# print(result)
for i, res in enumerate(result):
    # print(res['class'][0])
    if res['class'][0] == 'title':
        if res.string:
            print(i, res.string.strip())
        else:
            print(i, res.a.string)