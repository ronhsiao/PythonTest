import requests
from bs4 import BeautifulSoup


res = requests.get('https://money.udn.com/money/story/5607/2403089')
res.encoding = 'utf' #指定編碼
soup = BeautifulSoup(res.text,"html5lib")                #指定html5lib解析器
soup2 = soup.select('#story_body_content p')    #指定定位元素
print (soup2)