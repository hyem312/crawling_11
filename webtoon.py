import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup
import csv

url_1 = 'https://comic.naver.com/index'
keyword = input('최근 10화 제목과 평점이 궁금한 웹툰의 제목을 입력해주세요. =>')
url_2 = 'https://comic.naver.com/search?keyword='+keyword

res_1 = requests.get(url_2)
res_1.raise_for_status()
soup = BeautifulSoup(res_1.text, "lxml")

webtoon = soup.find("h5")
link = webtoon.a["href"]
url_3 = 'https://comic.naver.com'+link

res_2 = requests.get(url_3)
res_2.raise_for_status()
soup_2 = BeautifulSoup(res_2.text, "lxml")

titles = soup_2.find_all("td", attrs={"class":"title"})
stars = soup_2.find_all("div", attrs={"class":"rating_type"})

num_1 = []
num_2 = []
file = []
for title in titles:
    name = title.a.get_text()
    num_1.append(name)
    
for star in stars:
    score = star.strong.get_text()
    num_2.append(score)

for i in range(10):
    print(f"제목: {num_1[i]} ,평점: {num_2[i]}")
    file.append(f"제목: {num_1[i]} ,평점: {num_2[i]}")

import pandas as pd
data=pd.DataFrame(file)
data.to_csv('./webtoons.csv')