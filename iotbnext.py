import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.bnext.com.tw/categories/iot"
# driver = webdriver.Chrome('D:/browser/chrome/chromedriver.exe')  # 用chrome浏览器打开
driver = webdriver.PhantomJS(executable_path='D:/browser/phantomjs/bin/phantomjs.exe')  # 用phantomjs
driver.get(url)
print("loading driver complete")

driver.encoding = 'utf'
dps = driver.page_source
soup = BeautifulSoup(dps, "lxml")

i = 0
links = []
j = 0
links1 = []
f = open('D:\TestIot.txt', 'a', encoding='UTF-8')
for soup2 in soup.select('.font_sty02'):

    links.append(soup2.parent['href'])
    res2 = requests.get(links[i])
    res2.encoding = 'utf'
    soup2 = BeautifulSoup(res2.text, "lxml")
    print("request" + str(i))
    i += 1
    time.sleep(3)

    for soup3 in soup2.select(
            '#article_view_body > div.main_block > div > div > div.content.htmlview > div > div.left p, h2'):  # 用for迴圈取 會按照網頁<p>順序依序取出
        # , #article_view_body > div.main_block > div > div > div.article_info.container-fluid > span 日期
        # print(soup3.get_text(separator="\n\n", strip=True))
        f.write(soup3.get_text(separator="\n\n", strip=True))

f.write("\n")
print("loading complete1")

loop = 0
rel = str(20)
while loop < 2:
    clicktimes = 0
    # try:
    while clicktimes < 1:
        driver.execute_script(
            '"' + "document.querySelector('#category_list_body > div.main_block > div > div.inner.container-fluid > div.layout_sty01 > div.left > div > div.more_btn').rel1 =" + rel + '"')
        driver.find_element_by_class_name('more_btn').click()
        print("click complete" + str(clicktimes))
        time.sleep(3)
        clicktimes = clicktimes + 1

    # except:
    #     print("error")
    # print(str(driver.find_element_by_class_name('more_btn').get_attribute("rel1")))
    # driver.execute_script("document.querySelector('#category_list_body > div.main_block > div > div.inner.container-fluid > div.layout_sty01 > div.left > div > div.more_btn').rel1 =50") # 更改rel1的值
    # print(str(driver.find_element_by_class_name('more_btn').get_attribute("rel1")))

    print("loading complete2")
    driver.encoding = 'utf'
    dps = driver.page_source
    # f1 = open('D:\pagesource.txt', 'w', encoding='UTF-8')
    soup = BeautifulSoup(dps, "lxml")  # 指定html5lib解析器 lxml亦可 , lxml速度較 html5lib 快
    # f1.write(str(soup))  # 存原始碼，檢查用
    # f1.close()




    for soup21 in soup.select('.font_sty02'):

        links1.append(soup21.parent['href'])
        res21 = requests.get(links1[j])
        res21.encoding = 'utf'
        soup21 = BeautifulSoup(res21.text, "lxml")
        print("request" + str(j))
        j += 1
        time.sleep(3)
        for soup31 in soup21.select(
                '#category_list_body > div.main_block > div > div.inner.container-fluid > div.layout_sty01 > div.left > div > div.tg_list p, h2'):  # 用for迴圈取 會按照網頁<p>順序依序取出
            # , #article_view_body > div.main_block > div > div > div.article_info.container-fluid > span 日期
            # print(soup3.get_text(separator="\n\n", strip=True))
            f.write(soup31.get_text(separator="\n\n", strip=True))
    rel = str(driver.find_element_by_class_name('more_btn').get_attribute("rel1"))
    print("loop" + str(loop))
    loop += 1
    f.write("\n")

f.close()
driver.close()
print(links[len(links) - 1])
