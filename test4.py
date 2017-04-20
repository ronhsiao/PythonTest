import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

# sys.setdefaultencoding('utf8') # 设置编码
#
# url = 'http://baike.baidu.com/starrank?fr=lemmaxianhua'
#
#
# driver = webdriver.Chrome('D:\chrome') # 创建一个driver用于打开网页，记得找到brew安装的chromedriver的位置，在创建driver的时候指定这个位置
# driver.get(url) # 打开网页
#
# name_counter = 1
# page = 0;
# while page < 50: # 共50页，这里是手工指定的
# 	soup = BeautifulSoup(driver.page_source, "html.parser")
# 	current_names = soup.select('div.ranking-table') # 选择器用ranking-table css class，可以取出包含本周、上周的两个table的div标签
# 	for current_name_list in current_names:
# 		# print current_name_list['data-cat']
# 		if current_name_list['data-cat'] == 'thisWeek': # 这次我只想抓取本周，如果想抓上周，改一下这里为lastWeek即可
# 			names = current_name_list.select('td.star-name > a') # beautifulsoup选择器语法
# 			counter = 0;
# 			for star_name in names:
# 				counter = counter + 1;
# 				print star_name.text # 明星的名字是a标签里面的文本，虽然a标签下面除了文本还有一个与文本同级别的img标签，但是.text输出的只是文本而已
# 				name_counter = name_counter + 1;
# 	driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click() # selenium的xpath用法，找到包含“下一页”的a标签去点击
# 	page = page + 1
# 	time.sleep(2) # 睡2秒让网页加载完再去读它的html代码
#
# print name_counter # 共爬取得明星的名字数量
# driver.quit()

# driver = webdriver.Chrome('D:/browser/chrome/chromedriver.exe')  # 用chrome浏览器打开
driver = webdriver.PhantomJS(executable_path='D:/browser/phantomjs/bin/phantomjs.exe')  # 用phantomjs
driver.get("https://www.bnext.com.tw/articles")  # 打开知乎我们要登录

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
