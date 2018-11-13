from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pyquery import PyQuery as pq
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 50)


def search():
    print("正在搜索")
    try:
        browser.get('https://www.taobao.com')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
        input.send_keys('美食')
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                           '#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return total.text
    except TimeoutError:
        return search()


def next_page(page_number):
    print("正在翻页", page_number)
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#mainsrp-pager > div > div > div > ul > li.item.next > a > span:nth-child(1)')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR,
            'mainsrp-pager > div > div > div > ul > li.item.active > span'
             ), str(page_number)))
        get_products()
    except TimeoutError:
        next_page(page_number)


def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text()
        }
        print(product)


def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1))
    for i in range(2, total + 1):
        next_page(i)


if __name__ == '__main__':
    main()