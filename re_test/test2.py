import re
import requests
import json
import time


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.132 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i.*?data-src="(.*?)".*?<a.*?>(.*?)</a.*?"releasetime">(.*?)</p>',
        re.S
    )
    results = re.findall(pattern, html)
    for result in results:
        yield {
            'index': result[0],
            'image': result[1],
            'title': result[2].strip(),
            'time': result[3].strip()[5:] if len(result[3]) > 5 else ''
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        # print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
