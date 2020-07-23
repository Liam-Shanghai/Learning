from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
# print(html)

#betifulsoup载入html
soup = BeautifulSoup(html, features='lxml')
print(soup.p)


"""
<a href="https://morvanzhou.github.io/tutorials/scraping">爬虫教程</a>
"""
all_href = soup.find_all('a')
print(all_href)
all_href = [l['href'] for l in all_href]
print('\n', all_href)
