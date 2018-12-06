import os
from multiprocessing.pool import Pool
import requests
from urllib.parse import urlencode
from hashlib import md5
import json
import re
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }


def get_page_index(offset, keyword):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'gallery'  # 这个找不到？
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # print(response.text)
            return response.text
    except RecursionError:
        print("连接错误")
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():  # 保证json数据里面含有data这个属性
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求详情页出错", url)
        return None


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    # 获取标题
    title = soup.select('title')[0].get_text()
    # 图片正则表达式对象
    images_pattern = re.compile('gallery: JSON.parse\("(.*?)"\)', re.S)
    result = re.search(images_pattern, html)
    # 替换不需要的数据
    json_images = re.sub(r'\\{1,2}', '', result.group(1))  # 去掉\
    print(json_images)
    if result:
         images_data = json.loads(json_images)
         if images_data and 'sub_images' in images_data.keys():
             sub_images = images_data.get('sub_images')
             # 转换成数组
             images = [item.get('url') for item in sub_images]
             # 下载图片
             for image in images: down_load_images(image)
             return{
                'title': title,
                'url': url,
                'images': images
             }


# 下载图片
def down_load_images(url):
    print('正在下载',url)
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            save_images(response.content)
        return None
    except RequestException:
        print('请求图片出错', url)
        return None


# 存储图片
def save_images(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def main(offset):
    html = get_page_index(offset, "街拍")
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html, url)
            print(result)


if __name__ == '__main__':
    main(0)