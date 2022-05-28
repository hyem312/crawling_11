import requests                                                      
from bs4 import BeautifulSoup   
                                
url="https://comic.naver.com/webtoon/weekday.nhn"                        
res=requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")

tab = soup.find('div',{'class':'col_selected'})                    
webtoons = tab.find_all('a',{'class':'title'})                       

name=[]
for webtoon in webtoons:
    title=webtoon.get_text()
    print(title)
    name.append(title)

import pandas as pd
data=pd.DataFrame(name)
data.to_csv('./data.csv')