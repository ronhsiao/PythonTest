import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver



# driver = webdriver.Chrome('D:/browser/chrome/chromedriver.exe')  # 用chrome浏览器打开
driver = webdriver.PhantomJS(executable_path='D:/browser/phantomjs/bin/phantomjs.exe')  # 用phantomjs
driver.get("https://www.bnext.com.tw/articles")

clicktimes = 0
while clicktimes < 3:
    driver.find_element_by_class_name('more_btn').click()
    time.sleep(1.5)
    clicktimes = clicktimes + 1

driver.encoding = 'utf'
soup = BeautifulSoup(driver.page_source, "lxml")  # 指定html5lib解析器 lxml亦可 , lxml速度較 html5lib 快

i = 0
links = []
f = open('D:\Test.txt', 'w', encoding='UTF-8')
for soup2 in soup.select('.font_sty02'):

    links.append(soup2.parent['href'])
    res2 = requests.get(links[i])
    i = i + 1
    res2.encoding = 'utf'
    soup2 = BeautifulSoup(res2.text, "lxml")

    for soup3 in soup2.select(
            '#article_view_body > div.main_block > div > div > div.content.htmlview > div > div.left p, h2, #article_view_body > div.main_block > div > div > div.article_info.container-fluid > span'):  # 用for迴圈取 會按照網頁<p>順序依序取出
        # print(soup3.get_text(separator="\n\n", strip=True))
        f.write(soup3.get_text(separator="\n\n", strip=True))

f.close()
print(links[len(links) - 1])
