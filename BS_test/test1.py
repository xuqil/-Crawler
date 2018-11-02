from bs4 import BeautifulSoup


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
    <p name="ddd" class="appintro-title"><b>豆瓣</b></p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>
'''

soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
# print(soup.title.string)
# print(soup.title)
# print(soup.head.title.string)
# print(soup.p.string)
# print(soup.title.name)

# print(soup.div.contents)
# print(soup.div.children)
# for i, child in enumerate(soup.div.children):
#     print(i, child)

# print(soup.div.descendants)
# for i, child in enumerate(soup.div.descendants):
#     print(i, child)

# print(soup.a.parent)
# print(list(enumerate(soup.a.parents)))

# print(list(enumerate(soup.a.next_siblings)))
# print(list(enumerate(soup.a.previous_siblings)))

# print(soup.find_all('a'))
# for ul in soup.find_all('div'):
#     print(ul.find_all('a'))
# print(soup.find_all(attrs={'id': 'top-nav-appintro'}))
# print(soup.find_all(attrs={'name': 'ddd'}))
# print(soup.find_all(id='top-nav-appintro'))
# print(soup.find_all(class_="download"))
# print(soup.find_all(text='iPhone'))

# print(soup.find(class_="download"))

# print(soup.select('.download'))
# print(soup.select('div a'))
# print(soup.select('#top-nav-appintro'))
# for ul in soup.select('div'):
#     # print(ul.select('a'))
#     print(ul['class'])
#     print(ul.attrs['class'])

for li in soup.select('a'):
    print(li.get_text())
