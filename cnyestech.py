import requests
import time
from bs4 import BeautifulSoup
import json
# import pymysql as mariadb

# conn = mariadb.connect(host='localhost',user='root',passwd='rh119879944',charset='utf8',db='sexyblocks')
# cur=conn.cursor()

url = "http://news.cnyes.com/api/v3/news/category/tech"
# Sat = 1462896000
# Eat = 1462982399
Sat = 1356969600  # 20130101 00點00分00秒
Eat = 1357055999  # 20130101 23點59分59秒
f = open('D:\cnyesTech.txt', 'a', encoding='UTF-8')
feed = 1
# z=1
while Sat < 1388505600:
    print("Sat=" + str(Sat))
    print("S start")
    page = 1
    lastpage = 1
    pl = {'startAt': Sat, 'endAt': Eat, 'limit': '30', 'page': page}
    print("check page =" + str(page))
    res = requests.get(url, params=pl)
    res.close()
    restoJson = res.json()
    resJson = json.dumps(restoJson)
    rdj = json.loads(resJson)
    print("page=" + str(page))
    lastpage = int(rdj['items']['last_page'])
    print("lastpage=" + str(lastpage))
    while (lastpage - page) != -1:
        dataid = 0
        iftotal = rdj['items']['total']
        iftotal30 = iftotal % 30
        if (lastpage - page) == 0 or int(iftotal) < 30:
            print("data<30 or lastpage")
            while dataid < iftotal30:
                print("last loading" + str(dataid))
                newsid = rdj['items']['data'][dataid]['newsId']
                newsurl = "http://news.cnyes.com/news/id/" + str(newsid)
                newsres = requests.get(newsurl, headers={"Accept": "image/webp,image/*,*/*;q=0.8",
                                                         "Accept-Encoding": "gzip, deflate, sdch",
                                                         "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4",
                                                         "Connection": "keep-alive",
                                                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"})
                newsres.encoding = 'utf'
                soup = BeautifulSoup(newsres.text, "lxml")
                newsres.close()
                # time.sleep(3)
                dfList = " "
                newvalue = []
                for soup2 in soup.select(
                        '._82F p'):  # 用for迴圈取 會按照網頁<p>順序依序取出
                    # article = soup2.get_text(strip=True)
                    # article2 = article.rstrip()
                    # dfList = dfList + article2
                    # articlefinal.append(dfList)
                # newvalue = [dfList, newsurl, z]
                # cur.execute("insert into 2crawler(Postvalue,Href,Postnumber) values(%s,%s,%s);", newvalue)
                    f.write(soup2.get_text(strip=True))
                # f.write("\n\n")
                # f.write("value" + str(feed))
                f.write("\n")
                feed += 1
                dataid += 1
                # z+=1
            page += 1
        else:
            print("data = nor")
            while dataid < 30:
                print("nor loading" + str(dataid))
                newsid = rdj['items']['data'][dataid]['newsId']
                newsurl = "http://news.cnyes.com/news/id/" + str(newsid)
                newsres = requests.get(newsurl, headers={"Accept": "image/webp,image/*,*/*;q=0.8",
                                                         "Accept-Encoding": "gzip, deflate, sdch",
                                                         "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4",
                                                         "Connection": "keep-alive",
                                                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"})
                newsres.encoding = 'utf'
                soup = BeautifulSoup(newsres.text, "lxml")
                newsres.close()
                # time.sleep(3)
                dfList = " "
                newvalue = []
                for soup2 in soup.select(
                        '._82F p'):  # 用for迴圈取 會按照網頁<p>順序依序取出
                #     article = soup2.get_text(strip=True)
                #     article2 = article.rstrip()
                #     dfList = dfList + article2
                #     # articlefinal.append(dfList)
                # newvalue = [dfList, newsurl, z]
                # cur.execute("insert into 2crawler(Postvalue,Href,Postnumber) values(%s,%s,%s);", newvalue)
                    f.write(soup2.get_text(strip=True))
                # f.write("\n\n")
                # f.write("value" + str(feed))
                f.write("\n")
                feed += 1
                dataid += 1
                # z += 1
            page += 1
    print("total page=" + str(page-1))
    Sat = Sat + 86400
    Eat = Eat + 86400
# conn.commit()
# conn.close()
f.close()
