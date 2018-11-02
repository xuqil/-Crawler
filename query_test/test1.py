from pyquery import PyQuery as pq

html = '''<!DOCTYPE html>
<html lang="zh-CN" class=" book-new-nav">
  <head>
    <title>
    豆瓣读书
</title>

  </head>
  <body>  
  <script>var _body_start = new Date();</script> 
    <link href="//img3.doubanio.com/dae/accounts/resources/984c231/shire/bundle.css" rel="stylesheet" type="text/css">
<div id="db-global-nav" class="global-nav">

<div class="wrap">
    Hello world!
    <p>hai ni hao</p>
    <div class="abc">你是谁</div>
</div>

  <div class="bd">

<div class="top-nav-info">
  <a href="https://www.douban.com/accounts/login?source=book" class="nav-login" rel="nofollow">登录</a>
  <a href="https://www.douban.com/accounts/register?source=book" class="nav-register" rel="nofollow">注册</a>
</div>


    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p name="ddd" class="appintro-title aa"><b>豆瓣</b></p>
    <p class="qrcode aa">扫码直接下载</p>
    <p>last</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
            <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
  </div>
  <div>lash-child</div>
</div>
'''

"""三种初始化"""
# doc = pq(html)
# print(doc('a'))
# print(type(doc('a')))

# doc = pq(url='https://www.baidu.com')
# print(doc('head'))

# doc = pq(filename='text.html')
# print(doc('head').__unicode__('utf-8'))

"""css选择器"""
doc = pq(html)
# print(doc('.bd .top-nav-info a'))

items = doc('div')

# print(items)
# lis = items.find('a')
# print(lis)

# lis = items.children()
# lis = items.children('.top-nav-info')
# print(lis)

# container = items.parent()
# container = items.parents()
# container = items.parents('#db-global-nav')
# print(container)

# itemss = doc('#top-nav-appintro .appintro-title.aa')
# print(itemss)
# cotainer = itemss.siblings()
# print(cotainer)

# results = doc('a').items()
# print(type(results))
# for result in results:
#     print(result)

# results = doc('.top-nav-info a')
# print(results)
# print(results.attr('href'))
# print(results.attr.href)
# print(results.text())

# print(items.html())

# results = doc('.appintro-title.aa')
# print(results)
# results.remove_class('aa')
# print(results)
# results.add_class('aa')
# print(results)

# results = doc('.qrcode.aa')
# print(results)
# results.attr('name', 'link')
# print(results)
# results.css('font-size', '14px')
# print(results)

# results = doc('.wrap')
# print(results.text())
# results.find('p').remove()
# print(results.text())
# results.find('div').remove()
# print(results.text())

li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
# li = doc('li:nth-child(2)')
# print(li)
# li = doc('li:gt(2)')
# print(li)
# li = doc('li:nth-child(2n)')
# print(li)
# li = doc('li:contains(second)')
# print(li)

