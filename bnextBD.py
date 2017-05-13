import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.bnext.com.tw/categories/bigdata"
f = open('D:\\source\\BD.txt', 'a', encoding='UTF-8')
rel = 0
rel2 = 1
while (rel - rel2) != 0:
    j = 0
    links1 = []
    driver = webdriver.PhantomJS(executable_path='D:/browser/phantomjs/bin/phantomjs.exe')  # 用phantomjs
    driver.get(url)
    print("loading driver complete")
    driver.execute_script("document.querySelector('div.more_btn').setAttribute('rel1','" + str(rel) + "')")
    rel2 = int(driver.find_element_by_class_name('more_btn').get_attribute("rel1"))
    driver.find_element_by_class_name('more_btn').click()
    time.sleep(3)
    print("click complete")
    driver.encoding = 'utf'
    dps = driver.page_source
    soup = BeautifulSoup(dps, "lxml")
    rel = int(driver.find_element_by_class_name('more_btn').get_attribute("rel1"))
    print("rel=" + str(rel) +"  "+"rel2=" + str(rel2))
    for soup21 in soup.select("div.tg_list div.item_title"):
        links1.append(soup21.parent['href'])
        res21 = requests.get(links1[j])
        res21.encoding = 'utf'
        soup21 = BeautifulSoup(res21.text, "lxml")
        print("request " + str(j))
        j += 1
        res21.close()
        dfList=""
        for soup31 in soup21.select(
                'div.left p'):  # 用for迴圈取 會按照網頁<p>順序依序取出
            article = soup31.get_text(strip=True)
            article2 = article.rstrip()
            dfList = dfList + article2
        f.write(dfList + "\n\n")
    driver.close()
f.close()