from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# browser.get('https:www.taobao.com')

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
# input = browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()

# url = 'http://runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')
# 获取元素
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))
# 获取文本值
# input = browser.find_element_by_class_name('zu-top-add-question')
# # print(input.text)
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

# url = 'http://runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('ifranemeResfult')
# source = browser.find_element_by_css_selector('#draggable')
# print(source)

# url = 'https://www.zhihu.com/explore'
# browser.implicitly_wait(10)
# browser.get(url)
# input = browser.find_element_by_class_name('zu-to-add-question')
# print(input)

url = 'https://www.taobao.com/'
browser.get(url)
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)