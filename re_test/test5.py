import re
import requests
import time


def get_page_one(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/63.0.3239.132 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    pattern_sub = re.compile(
        '<i class="integer">|</i><i class="fraction">|</i>',
        re.S
    )
    pattern = re.compile(
        '<dd>.*?<img.*?data-src="(.*?)".*?</div.*?movie-item-title.*?title="(.*?)".*?<div.*?orange">(.*?)</div>',
        re.S
    )
    results = re.sub(pattern_sub, '', html)
    results = re.findall(pattern, results)
    for result in results:
        yield {
            'image': result[0],
            'title': result[1],
            'sore': result[2].strip(),
            # 'time': result[3].strip()[5:] if len(result[3]) > 5 else ''
        }


def main():
    url = 'http://maoyan.com/films?offset=0'
    html = get_page_one(url)
    for item in parse_one_page(html):
        print(item)


main()