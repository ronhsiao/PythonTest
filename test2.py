
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.bnext.com.tw/articles")
res.encoding = 'utf'
soup = BeautifulSoup(res.text,"lxml")                                   #指定html5lib解析器 lxml亦可 , lxml速度較 html5lib 快

# for soup2 in soup.select('.container-fluid .div_td .item_summary'):                       #用for迴圈取 會按照網頁<p>順序依序取出
#     print(soup2.get_text(separator="\n\n",strip=True))                                      #只取內容 去除<p>
i = 0
links = []
for soup2 in soup.select('.font_sty02'):

    links.append(soup2.parent['href'])
    res2 = requests.get(links[i])
    i = i+1
    res2.encoding = 'utf'
    soup2 = BeautifulSoup(res2.text,"lxml")
    for soup3 in soup2.select('#article_view_body > div.main_block > div > div > div.content.htmlview > div > div.left p, h2'):                       #用for迴圈取 會按照網頁<p>順序依序取出
        print(soup3.get_text(separator="\n\n",strip=True))
#  print(len(links))
# print(links)
