import requests
from bs4 import BeautifulSoup

# https://buzzorange.com/techorange/?s=AR+VR
# https://buzzorange.com/techorange/page/2/?s=AR+VR
f = open('D:\\buzzAI.txt', 'a', encoding='UTF-8')
k = 1
links = []
j = 0
url = "https://buzzorange.com/techorange/?s=%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7"
x = 1
while x < 90:
    res = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"})
    res.encoding = 'utf'
    soup = BeautifulSoup(res.text, "lxml")
    res.close()
    for souplink in soup.select(" header > h4"):
        links.append(souplink.a['href'])
        feedres = requests.get(links[j], headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"})
        feedres.encoding = 'utf'
        soupfeeds = BeautifulSoup(feedres.text, "lxml")
        feedres.close()
        print("value"+str(k))
        for soupfeed in soupfeeds.select(
                '#main p'):  # 用for迴圈取 會按照網頁<p>順序依序取出
            f.write(soupfeed.get_text(separator="\n\n", strip=True))
        f.write("\n\n")
        f.write("value" + str(k))
        k += 1
        f.write("\n\n")
        j += 1
    x += 1
    url = "https://buzzorange.com/techorange/page/" + str(x) + "/?s=%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7"
    print("page" + str(x))
f.close()
