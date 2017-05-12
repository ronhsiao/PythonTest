import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pymysql as mariadb

conn = mariadb.connect(host='localhost', user='root', passwd='rh119879944', charset='utf8', db='sexyblocks')
cur = conn.cursor()
url = "https://www.bnext.com.tw/categories/ai"
rel = 0
rel2 = 1
k = 1

# while (rel-rel2)!=0:
while rel < 48:
    j = 0
    links1 = []
    driver = webdriver.PhantomJS(executable_path='D:/browser/phantomjs/bin/phantomjs.exe')
    driver.get(url)
    # print("loading driver complete")
    driver.execute_script("document.querySelector('div.more_btn').setAttribute('rel1','" + str(rel) + "')")
    rel2 = int(driver.find_element_by_class_name('more_btn').get_attribute("rel1"))
    driver.find_element_by_class_name('more_btn').click()
    time.sleep(3)
    # print("loading complete2")
    driver.encoding = 'utf'
    dps = driver.page_source
    soup = BeautifulSoup(dps, "lxml")
    rel = int(driver.find_element_by_class_name('more_btn').get_attribute("rel1"))
    for soup21 in soup.select("div.tg_list div.item_title"):
        links1.append(soup21.parent['href'])
        res21 = requests.get(links1[j])
        res21.encoding = 'utf'
        soup21 = BeautifulSoup(res21.text, "lxml")
        time.sleep(3)


        dfList = " "
        newvalue = []
        for soup31 in soup21.select(
                '#article_view_body > div.main_block > div > div > div.content.htmlview > div > div.left > article.main_content'):
            article = soup31.get_text(strip=True)
            article2 = article.rstrip()
            dfList = dfList + article2
        print(dfList)
        newvalue = [dfList, links1[j],k]
        cur.execute("insert into 2crawler(Postvalue,Href,Postnumber) values(%s,%s,%s);", newvalue)
        j += 1
        k += 1
    # df = pd.DataFrame(articlefinal)
    driver.close()
    # df.to_csv('bnextAI.csv')
conn.commit()
conn.close()
