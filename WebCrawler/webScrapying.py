import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.ptt.cc/bbs/movie/index.html")
good = []
normal = []
bad = []

for i in range(0,10):
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.findAll("div", class_="title")
    for title in titles:
        if(title.select_one("a") is not None):
            text = title.select_one("a").getText()
            if text.startswith('[好雷]'):
                good.append(text)
            elif text.startswith('[普雷]'):
                normal.append(text)
            elif text.startswith('[負雷]'):
                bad.append(text)               
    
    links = soup.findAll("a", class_="btn wide", href=True)
    url = "https://www.ptt.cc/" + links[1]['href']
    response = requests.get(url)

with open('movie.txt', 'w', encoding='UTF-8') as f:
        f.write('\n'.join(good))
        f.write('\n'.join(normal))
        f.write('\n'.join(bad))
        f.close()