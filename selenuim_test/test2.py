from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https:www.taobao.com')

# 获取单个元素
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# # input_third = browser.find_element_by_xpath('//*[@id="q"')
# print(input_first, input_second)
# browser.close()

# 获取多个元素
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)
for li in lis:
    print(li)
browser.close()