import json
from bs4 import BeautifulSoup
import requests
op=open('scrap.json')
data_dic,ask,check={},int(input('tell the rank of the movie you wanna see:- ')),json.load(op)
for i in check:
    if i['Rank']==ask:
        url=i["Link"]
page=requests.get(url) 
soup=BeautifulSoup(page.text,"html.parser")
body_of_web=soup.find('div',{'id':'__next'})
structure=body_of_web.find('main')
sturct=structure.find('div', class_='ipc-page-content-container ipc-page-content-container--full BaseLayout__NextPageContentContainer-sc-180q5jf-0 fWxmdE')
section=sturct.find('section', class_='ipc-page-background ipc-page-background--base TitlePage__StyledPageBackground-wzlr49-0 dDUGgO')
sctor=section.find('section', class_='ipc-page-background ipc-page-background--baseAlt TitleMainHeroGroup__StyledPageBackground-w70azj-0 hEHQFC')
division=sctor.find('div', class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt")
genre=sctor.find('div', class_="GenresAndPlot__ContentParent-cum89p-8 bFvaWW Hero__GenresAndPlotContainer-kvkd64-11 twqaW")
b=genre.find_all('a', class_='GenresAndPlot__GenreChip-cum89p-3 fzmeux ipc-chip ipc-chip--on-baseAlt')
genr=[]
for i in b:
    genr.append(i.text)
bio=genre.find('span', class_='GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD').text
if len(division.text[-7::])!=7:
    time=division.text[-7::]
else:
    time=division.text[-8::]
name=division.find('h1').text
print(time)
time2=int(time[0])*60
if 'min' in time:
    a=time.strip('min').split('h')
    run_time=str(time2+int(a[1]))+' minutes'
director=structure.find('a',class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').text
country_and_more= structure.find_all('li', class_='ipc-metadata-list__item')
for i in country_and_more:
    if 'Country of origin' in i.text:
        country=i.text[17:]
    if 'Language' in i.text:
        language=i.text[8:]
if 'Read all' in bio:
    bio=bio[0:-8]
img=structure.find('div',class_='Media__PosterContainer-sc-1x98dcb-1 dGdktI')
link='https://www.imdb.com/'+(body_of_web.find_all("div",class_="ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width ipc-sub-grid-item ipc-sub-grid-item--span-2")[0].a['href'])
print(language,'\n',country,'\n',run_time,'\n',director,'\n',genr,'\n',bio,'\n',name,'\n',link)
