import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from requests import Request, Session
import json

url = "http://news.cnyes.com/api/v2/news"

pl = {'startAt': '1492272000', 'endAt': '1493222399', 'limit': '30'}
headers = {"User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
res = requests.get(url, params=pl).json()

# test = json(res)
print(res)
