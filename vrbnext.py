import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.bnext.com.tw/categories/vr"
f = open('D:\TestVR.txt', 'a', encoding='UTF-8')
rel = 0
rel2 = 1
clicktimes = 1
k = 1
while (rel - rel2) != 0:
    j = 0
    links1 = []
    driver = webdriver.PhantomJS(executable_path='D:/browser/phantomjs/bin/phantomjs.exe')  # 用phantomjs
    driver.get(url)
    print("loading driver complete")
    driver.execute_script("document.querySelector('div.more_btn').setAttribute('rel1','" + str(rel) + "')")
    rel2 = int(driver.find_element_by_class_name('more_btn').get_attribute("rel1"))
    driver.find_element_by_class_name('more_btn').click()
    # time.sleep(3)
    print("loading complete2")
    driver.encoding = 'utf'
    dps = driver.page_source
    soup = BeautifulSoup(dps, "lxml")
    rel = int(driver.find_element_by_class_name('more_btn').get_attribute("rel1"))
    for soup21 in soup.select("#page_2_ .sitem_title, .font_sty02"):
        links1.append(soup21.parent['href'])
        res21 = requests.get(links1[j])
        res21.encoding = 'utf'
        soup21 = BeautifulSoup(res21.text, "lxml")
        print("request" + str(j))
        j += 1
        time.sleep(2)
        for soup31 in soup21.select(
                '#article_view_body > div.main_block > div > div > div.content.htmlview > div > div.left p'):  # 用for迴圈取 會按照網頁<p>順序依序取出
            f.write(soup31.get_text(separator="\n\n", strip=True))
        f.write("\n\n")
        f.write("value" + str(k))
        k += 1
        f.write("\n\n")
    print("loop" + str(clicktimes))
    clicktimes = clicktimes + 1

    f.write("\n\n")
    driver.close()

f.close()
# print(len(links))
# print(links1[len(links1) - 1])
