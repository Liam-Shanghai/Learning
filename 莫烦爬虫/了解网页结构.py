from urllib.request import urlopen
import re

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)

#正则表达式爬取<title></title>中的内容
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])

"""
如果想要找到中间的那个段落 <p>,
我们使用下面方法, 因为这个段落在 HTML 中还夹杂着 tab, new line,
所以我们给一个 flags=re.DOTALL 来对这些 tab, new line 不敏感.
"""
res=re.findall(r"<p>(.+?)</p>",html,flags=re.DOTALL)
print("\nPage paragraph is: ", res[0])

#寻找所有的链接
res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)