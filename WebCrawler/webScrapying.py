from locale import normalize
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(".\chromedriver.exe")
driver.get("https://www.ptt.cc/bbs/movie/index.html")

good = []
normal = []
bad = []

for i in range(0,10):
    soup = BeautifulSoup(driver.page_source, "html.parser")
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

    link = driver.find_element(By.LINK_TEXT,"‹ 上頁")
    link.click()
#print(soup.prettify())  #輸出排版後的HTML內容
driver.close() # 關閉瀏覽器視窗


with open('movie.txt', 'w', encoding='UTF-8') as f:
        f.write('\n'.join(good))
        f.write('\n'.join(normal))
        f.write('\n'.join(bad))
        f.close()   
