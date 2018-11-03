from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https:www.taobao.com')

# 获取单个元素
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# # input_third = browser.find_element_by_xpath('//*[@id="q"')
# print(input_first, input_second)
# browser.close()

# 获取多个元素
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
# for li in lis:
#     print(li)
# browser.close()

#元素交互操作
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()